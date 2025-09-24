from math import gcd


def reduce_numbers(n: int, m: int) -> tuple[int, int]:
    return n // gcd(n, m), m // gcd(n, m)


def get_sqrt_representation(number: int) -> tuple[list[int], list[int]]:
    """
    Algorithm steps:
    1. start with numerator = 1, a_0 = k = floor(number ** 0.5)
    2. while True:
        a. a_current = floor(numerator / (number - k)) = floor((numerator * number ** 0.5) / (number - k ** 2))
        b. reduce numerator and denominator
        c. update:
            k = a_current * denominator - k * numerator
            numerator = denominator
        d. if (a_current, numerator, k) has been seen, it's a cycle.
    """
    number_sqrt = number ** 0.5
    if number_sqrt == int(number_sqrt):
        return [int(number_sqrt)], []
    numerator, k = 1, int(number_sqrt)
    representation = [(k, numerator, k)]
    while True:
        # Calculate the current element
        denominator = number - k ** 2
        current_number = numerator * (number_sqrt + k) / denominator
        a_current = int(current_number)
        # Update the variables
        numerator, denominator = reduce_numbers(numerator, denominator)
        k = a_current * denominator - k * numerator
        numerator = denominator
        # Check if the current variables set has been seen
        if (a_current, numerator, k) in representation:
            # Fetch the prefix and cycle from the representation
            index = representation.index((a_current, numerator, k))
            prefix, cycle = representation[:index], representation[index:]
            prefix = list(map(lambda x: x[0], prefix))
            cycle = list(map(lambda x: x[0], cycle))
            return prefix, cycle
        representation.append((a_current, numerator, k))
