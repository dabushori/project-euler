DIGITS = set(map(str, range(1, 10)))


def is_one_to_nine_pandigital(number: int | str):
    number = str(number)
    return len(number) == len(DIGITS) and set(number) == DIGITS


def _get_pandigital_numbers_custom_digits(digits: list[int], as_strings: bool):
    if len(digits) < 1:
        raise ValueError("Invalid digits argument")
    elif len(digits) == 1:
        yield str(digits[0]) if as_strings else digits[0]
    else:
        for index, digit in enumerate(digits):
            remaining_digits = digits[:index] + digits[index + 1:]
            for remainder in _get_pandigital_numbers_custom_digits(remaining_digits, as_strings):
                yield f'{digit}{remainder}' if as_strings else int(f'{digit}{remainder}')


def get_pandigital_numbers(max_n: int, as_strings: bool = False):
    """
    This function generates all the 1 to max_n pandigital numbers.
    """
    yield from _get_pandigital_numbers_custom_digits(list(range(1, max_n + 1)), as_strings)


def get_pandigital_numbers_in_custom_range(start: int, end: int, as_strings: bool = False):
    """
    This function generates all the start to end pandigital numbers.
    """
    if not (0 <= start <= 9 and 0 <= end <= 9):
        raise ValueError("Invalid start or end")
    yield from _get_pandigital_numbers_custom_digits(list(range(start, end + 1)), as_strings)
