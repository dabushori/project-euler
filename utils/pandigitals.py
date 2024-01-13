DIGITS = set(map(str, range(1, 10)))


def is_one_to_nine_pandigital(number: int | str):
    number = str(number)
    return len(number) == len(DIGITS) and set(number) == DIGITS
