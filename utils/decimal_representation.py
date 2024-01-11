def decimal_representation_with_remainders(numerator: int, denominator: int):
    """
    Yield the numbers after the dot, and the remainders if specified.
    """
    if numerator // denominator == numerator / denominator:
        return
    remainder = 10 * (numerator % denominator)
    while True:
        digit = remainder // denominator
        remainder = 10 * (remainder - digit * denominator)
        yield digit, remainder
        if remainder % denominator == 0:
            break


def decimal_representation(numerator: int, denominator: int, precision: int | None = None):
    """
    Yield the numbers after the dot, and the remainders if specified.
    """
    if precision is not None and precision <= 0:
        raise ValueError("Invalid precision")
    if numerator // denominator == numerator / denominator:
        return
    index = 0
    remainder = 10 * (numerator % denominator)
    while True:
        digit = remainder // denominator
        remainder = 10 * (remainder - digit * denominator)
        if precision is not None and index >= precision:
            return
        yield digit
        index += 1
        if remainder % denominator == 0:
            break


def get_recurring_cycle(numerator: int, denominator: int) -> tuple[int | None, int]:
    """
    The return value of this function is a tuple (index, length) where index is the index of the start of the recurring
    cycle, and length is the length of the cycle. In case there's no cycle (finite representation), index will be None
    and length will be 0.
    """
    digits = dict()
    decimal_representation_generator = decimal_representation_with_remainders(numerator, denominator)
    for index, (digit, remainder) in enumerate(decimal_representation_generator, start=1):
        if (digit, remainder) in digits:
            return digits[(digit, remainder)], len(digits) - digits[(digit, remainder)] + 1
        digits[(digit, remainder)] = index
    return None, 0
