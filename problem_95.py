"""
Challenge 95 of project euler - Amicable Chains

@author Ori Dabush
"""

from functools import cache
from utils.divisors import get_divisors


UPPER_LIMIT = 1_000_000


@cache
def sum_of_proper_divisors(n: int) -> int:
    return sum(get_divisors(n)) - n


def solve():
    chains = []
    numbers_visited = set()
    for n in range(1, UPPER_LIMIT + 1):
        current_number = n
        chain = [n]
        while True:
            current_number = sum_of_proper_divisors(current_number)
            # If the number is invalid, invalidate the chain and break
            if not 1 <= current_number <= UPPER_LIMIT:
                chain = []
                break
            # If the current number is in the chain, a chain was closed.
            # It can be a chain that starts not from the first element, so take it from the current element.
            if current_number in chain:
                chain = chain[chain.index(current_number):]
                break
            # If the current number has already seen we already marked this chain, so break and invalidate the chain
            if current_number in numbers_visited:
                chain = []
                break
            # Add the current number to the chain and to the visited numbers set
            chain.append(current_number)
            numbers_visited.add(current_number)
        if chain:
            chains.append(chain)
    return min(max(chains, key=len))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
