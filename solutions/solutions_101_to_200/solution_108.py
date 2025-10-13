"""
Challenge 110 of project euler - Diophantine Reciprocals II

@author Ori Dabush
"""

from math import prod, inf
from solutions.utils.primes import get_first_n_primes


TARGET_VALUE = 1000


def number_of_solutions(powers):
    return (prod(2 * p + 1 for p in powers) + 1) // 2


def n_from_prime_factors(powers):
    """
    Calculate the minimal number which can be created using the given primes factors (assuming they are
    sorted in decreasing order).

    This function will take the first `len(powers)` prime numbers and will calculate the value of n.
    """
    primes = get_first_n_primes(len(powers))
    return prod((base ** power) for base, power in zip(primes, powers))


def solve():
    """
    Read more about this algorithm in solution_110.py.
    """
    queue = [[0]]
    minimal_number_found = inf
    while queue:
        powers = queue.pop(0)
        number = n_from_prime_factors(powers)
        if number >= minimal_number_found:
            continue
        if number_of_solutions(powers) > TARGET_VALUE:
            # If we reached the target value, check if this is the minimal value
            minimal_number_found = min(minimal_number_found, number)
        else:
            # Now, we can add one to the current power
            new_powers = powers.copy()
            if len(new_powers) == 1 or new_powers[-2] >= new_powers[-1] + 1:
                new_powers.append(new_powers.pop() + 1)
                queue.append(new_powers)
            # Or we can add a new power
            queue.append(powers.copy() + [1])
    return minimal_number_found

def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
