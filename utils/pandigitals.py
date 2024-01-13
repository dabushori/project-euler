DIGITS = set(map(str, range(1, 10)))


def is_one_to_nine_pandigital(number: int | str):
    number = str(number)
    return len(number) == len(DIGITS) and set(number) == DIGITS


def _get_pandigital_numbers_custom_digits(digits: list[int]):
    if len(digits) < 1:
        raise ValueError("Invalid digits argument")
    elif len(digits) == 1:
        yield digits[0]
    else:
        for index, digit in enumerate(digits):
            remaining_digits = digits[:index] + digits[index + 1:]
            for remainder in _get_pandigital_numbers_custom_digits(remaining_digits):
                yield int(f'{digit}{remainder}')


def get_pandigital_numbers(max_n: int):
    yield from _get_pandigital_numbers_custom_digits(list(range(1, max_n + 1)))
