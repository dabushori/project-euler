"""
Challenge 110 of project euler - Diophantine Reciprocals II

@author Ori Dabush
"""

from math import prod, inf
from solutions.utils.primes import get_first_n_primes


TARGET_VALUE = 4_000_000


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
    I found out that the number of solutions is based on the powers of the prime factors of n and
    is given by the formula implemented in the `number_of_solutions` function.

    Because the order of the powers does not matter, we know that the minimal number we are looking for 
    will be of the form:
    n = (p1 ** n1) * ... * (pk ** nk)
    where p1 < ... < pk and n1 >= ... >= nk
    (If it wasn't like this, we could have sort them and find a smaller value of n with the same number of solutions).

    So I implemented the logic to go through all the possible combinations of powers in decreasing order and found the
    minimal n which gives at least 4000000 different solutions.
    
    I optimized the code by:
    * using loops and not recursion
    * stopping if we reach a number which is greater than the minimum we already found
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
