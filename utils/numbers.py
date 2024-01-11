THOUSAND = 'thousand'
HUNDRED = 'hundred'
DIGITS = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}
TEEN_NUMBERS = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}
TEN_NUMBERS = {
    10: 'ten',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}


def number_to_words(number: int) -> str:
    if number > 1000 or number < 0:
        raise NotImplementedError(f'Converting {number} to words is not implemented currently')
    # [1000]
    if number == 1000:
        return f'{number_to_words(number // 1000)} {THOUSAND}'
    # [100, 999]
    if number >= 100:
        if number % 100:
            return f'{number_to_words(number // 100)} {HUNDRED} and {number_to_words(number % 100)}'
        else:
            return f'{number_to_words(number // 100)} {HUNDRED}'
    # [10, 99]
    if number >= 10:
        if number % 10 == 0:
            return TEN_NUMBERS[number]
        if number < 20:
            return TEEN_NUMBERS[number]
        return f'{number_to_words(number - number % 10)}-{number_to_words(number % 10)}'
    # [0, 9]
    return DIGITS[number]
