"""
Challenge 54 of project euler - Poker Hands

@author Ori Dabush
"""

from collections import Counter
from enum import StrEnum, IntEnum
from utils.inputs import get_input


class CardSuit(StrEnum):
    HEART = 'H'
    DIAMOND = 'D'
    SPADE = 'S'
    CLOVER = 'C'


class CardValue(StrEnum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = 'T'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'


class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10


VALUES_ORDER = [
    CardValue.TWO,
    CardValue.THREE,
    CardValue.FOUR,
    CardValue.FIVE,
    CardValue.SIX,
    CardValue.SEVEN,
    CardValue.EIGHT,
    CardValue.NINE,
    CardValue.TEN,
    CardValue.JACK,
    CardValue.QUEEN,
    CardValue.KING,
    CardValue.ACE,
]
HAND_SIZE = 5
ROYAL_FLUSH_MIN_VALUE = CardValue.TEN


class Card:
    def __init__(self, card_string: str):
        if len(card_string) != 2:
            raise ValueError(f'Invalid card string: {card_string}')
        self.value = CardValue(card_string[0])
        self.suit = CardSuit(card_string[1])

    def __str__(self):
        return f'{self.value}{self.suit}'

    def __repr__(self):
        return f'{self.value}{self.suit}'


def is_flush(card_suits: list[CardSuit]) -> bool:
    """
    Return whether all the suits are the same or not.
    """
    return len(set(card_suits)) == 1


def is_straight(card_values: list[CardValue]) -> bool:
    """
    Return whether the cards are consecutive values.
    """
    indexes = [VALUES_ORDER.index(value) for value in card_values]
    min_value_index = min(indexes)
    return all(min_value_index + i in indexes for i in range(HAND_SIZE))


def get_hand_type(cards: list[Card]) -> tuple[HandType, list[CardValue]]:
    """
    This function returns a tuple containing the hand type and the list of high card sorted.
    The cards from the hand appear first, then the rest of the cards in descending order.
    """
    value_counter = Counter(getattr(card, 'value') for card in cards)
    suit_counter = Counter(getattr(card, 'suit') for card in cards)
    _is_flush = is_flush(list(suit_counter.keys()))
    _is_straight = is_straight(list(value_counter.keys()))
    most_common_value, second_most_common_value = value_counter.most_common(2)
    if _is_flush:
        min_value = min(value_counter.keys(), key=VALUES_ORDER.index)
        if min_value == ROYAL_FLUSH_MIN_VALUE:
            return HandType.ROYAL_FLUSH, [min_value, second_most_common_value[0]]
        elif _is_straight:
            return HandType.STRAIGHT_FLUSH, [min_value, second_most_common_value[0]]
    if most_common_value[1] == 4:
        return HandType.FOUR_OF_A_KIND, sorted(
            [most_common_value[0], second_most_common_value[0]], key=VALUES_ORDER.index, reverse=True
        )
    if most_common_value[1] == 3 and second_most_common_value[1] == 2:
        return HandType.FULL_HOUSE, sorted(
            [most_common_value[0], second_most_common_value[0]], key=VALUES_ORDER.index, reverse=True
        )
    if _is_flush:
        return HandType.FLUSH, sorted(list(value_counter.keys()), key=VALUES_ORDER.index, reverse=True)
    if _is_straight:
        return HandType.STRAIGHT, sorted(list(value_counter.keys()), key=VALUES_ORDER.index, reverse=True)
    if most_common_value[1] == 3:
        return HandType.THREE_OF_A_KIND, [most_common_value[0]] + sorted(
            [value for value, _ in value_counter.most_common(3)[1:]], key=VALUES_ORDER.index, reverse=True
        )
    if most_common_value[1] == 2:
        if second_most_common_value[1] == 2:
            return (HandType.TWO_PAIRS, [
                max(most_common_value[0], second_most_common_value[0], key=VALUES_ORDER.index),
                min(most_common_value[0], second_most_common_value[0], key=VALUES_ORDER.index),
                value_counter.most_common(3)[2][0]
            ])
        else:
            return HandType.ONE_PAIR, [most_common_value[0]] + sorted(
                [value for value, _ in value_counter.most_common(4)[1:]], key=VALUES_ORDER.index, reverse=True
            )
    return HandType.HIGH_CARD, sorted(list(value_counter.keys()), key=VALUES_ORDER.index, reverse=True)


class Hand:
    def __init__(self, cards_strings: list[str]):
        if len(cards_strings) != HAND_SIZE:
            raise ValueError(f'Invalid card strings: {cards_strings}')
        self.cards = [Card(card_string) for card_string in cards_strings]
        self.hand_type, self.high_cards = get_hand_type(self.cards)

    def wins(self, other: 'Hand') -> bool:
        """
        Return whether self wins other or not.
        """
        if self.hand_type != other.hand_type:
            return bool(self.hand_type > other.hand_type)
        for self_high_card, other_high_card in zip(self.high_cards, other.high_cards):
            if self_high_card != other_high_card:
                return bool(VALUES_ORDER.index(self_high_card) > VALUES_ORDER.index(other_high_card))
        raise ValueError('Somehow we got a tie')


def solve():
    lines = get_input(54).split('\n')
    games = [(Hand(line.split(' ')[:HAND_SIZE]), Hand(line.split(' ')[HAND_SIZE:])) for line in lines]
    return len([game for game in games if game[0].wins(game[1])])


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
