"""
Challenge 88 of project euler - Product-sum Numbers

@author Ori Dabush
"""

from utils.sorted_tuple import SortedTuple
from utils.primes import is_prime, get_prime_factors
from itertools import count
from functools import reduce
from operator import mul


MIN_K, MAX_K = 2, 12_000


def get_all_factors_multiplications(n: int) -> set[SortedTuple[int, ...]]:
    """
    Get all the combinations of prime factor multiplications.
    For example:
    - for n = 16 the output is {(4, 4), (2, 2, 2, 2), (2, 2, 4), (16,), (2, 8)}
    - for n = 210 the output is:
        {(10, 21), (2, 3, 35), (3, 7, 10), (2, 5, 21),
         (2, 3, 5, 7), (6, 35), (2, 7, 15), (210,), (5, 6, 7),
         (5, 42), (2, 105), (3, 70), (3, 5, 14), (14, 15), (7, 30)}
    """
    if n == 1 or is_prime(n):
        return {SortedTuple([n])}
    results = set()
    # Iterate over every unique factor
    for factor in set(get_prime_factors(n)):
        # For every multiplication of the rest of the number, multiply the factor by each element of the product
        for multiplication in get_all_factors_multiplications(n // factor):
            multiplication = list(multiplication)
            for other_factor in set(multiplication):
                # Multiply other_factor by factor
                new_mult = multiplication.copy()
                new_mult.remove(other_factor)
                new_mult.append(factor * other_factor)
                # Use a sorted tuple to avoid duplications
                results.add(SortedTuple(new_mult))
            # Add the factor as an additional element in the multiplication
            multiplication.append(factor)
            # Use a sorted tuple to avoid duplications
            results.add(SortedTuple(multiplication))
    return results


def solve():
    """
    For every number we find all the combinations of its product, and we find the k that it satisfies by adding 1s
    until the sum is equal to the product. We keep doing it until we find the minimal product-sum number for each
    value of k.
    """
    results = {}
    for n in count(start=2):
        if len(results) == MAX_K - MIN_K + 1:
            return sum(set(results.values()))
        for multiplication in get_all_factors_multiplications(n):
            result_prod = reduce(mul, multiplication)
            result_sum = sum(multiplication)
            if result_sum > result_prod:
                continue
            k = len(multiplication) + (result_prod - result_sum)
            if k in results or not (MIN_K <= k <= MAX_K):
                continue
            results[k] = result_prod


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
