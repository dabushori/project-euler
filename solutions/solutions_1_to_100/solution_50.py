"""
Challenge 50 of project euler - Consecutive Prime Sum

@author Ori Dabush
"""

from solutions.utils.primes import prime_numbers_until_with_space


UPPER_LIMIT = 1_000_000
PRIMES_BELOW_LIMIT_SET = set(prime_numbers_until_with_space(UPPER_LIMIT))
PRIMES_BELOW_LIMIT_SORTED_LIST = sorted(PRIMES_BELOW_LIMIT_SET)


def solve():
    max_sum_value, max_sum_length = 0, 0
    for sum_start_index, sum_start in enumerate(PRIMES_BELOW_LIMIT_SORTED_LIST):
        # For every prime number iterate on the sum length starting from the max length found so far until a length
        # which leads to the end of the primes list.
        for sum_length in range(max_sum_length, len(PRIMES_BELOW_LIMIT_SET) - sum_start_index):
            sum_value = sum(PRIMES_BELOW_LIMIT_SORTED_LIST[sum_start_index:sum_start_index + sum_length])
            # Stop if the sum passes the upper limit
            if sum_value >= UPPER_LIMIT:
                break
            # If the sum is prime we got a longer sum
            if sum_value in PRIMES_BELOW_LIMIT_SET:
                max_sum_value = sum_value
                max_sum_length = sum_length
    return max_sum_value


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
