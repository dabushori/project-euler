"""
Challenge 89 of project euler - Roman Numerals

@author Ori Dabush
"""

from utils.inputs import get_input


ROMAN_LETTER_TO_VALUE = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

VALUE_TO_ROMAN_LETTER = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
}


def roman_to_int(roman: str) -> int:
    result = 0
    while True:
        index = 0
        current_result = 0
        while index < len(roman) and roman[index] == roman[0]:
            current_result += ROMAN_LETTER_TO_VALUE[roman[0]]
            index += 1
        if index == len(roman):
            result += current_result
            return result
        if ROMAN_LETTER_TO_VALUE[roman[index]] > ROMAN_LETTER_TO_VALUE[roman[0]]:
            result -= current_result
        else:
            result += current_result
        roman = roman[index:]


def digit_to_roman(digit: int, base: int) -> str:
    """
    The logic for (1, 5, 10), (10, 50, 100) and (100, 500, 1000) is identical, it's just the letters which are different
    """
    unit_char = VALUE_TO_ROMAN_LETTER[base]
    five_char = VALUE_TO_ROMAN_LETTER[base * 5]
    ten_char = VALUE_TO_ROMAN_LETTER[base * 10]
    if 0 <= digit <= 3:
        return digit * unit_char
    elif 4 <= digit <= 5:
        return (5 - digit) * unit_char + five_char
    elif 6 <= digit <= 8:
        return five_char + (digit - 5) * unit_char
    elif 9 <= digit <= 10:
        return (10 - digit) * unit_char + ten_char


def int_to_roman(number: int) -> str:
    if number == 0:
        return ''
    if number in VALUE_TO_ROMAN_LETTER:
        return VALUE_TO_ROMAN_LETTER[number]

    # Get the thousands, hundreds, tens and units of the number
    thousands, remainder = number // 1000, number % 1000
    hundreds, remainder = remainder // 100, remainder % 100
    tens, units = remainder // 10, remainder % 10

    # Convert each of them to roman
    thousands = VALUE_TO_ROMAN_LETTER[1000] * thousands
    hundreds = digit_to_roman(hundreds, 100)
    tens = digit_to_roman(tens, 10)
    units = digit_to_roman(units, 1)

    # Concatenate them together
    return thousands + hundreds + tens + units


def solve():
    """
    We assume that the roman numerals are valid., and that they contain no more than four consecutive identical units.
    """
    romans = get_input(89).split()
    return sum(len(roman) - len(int_to_roman(roman_to_int(roman))) for roman in romans)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
