"""
Challenge 103 of project euler - Special Subset Sums: Optimum

@author Ori Dabush
"""

from itertools import combinations
from solutions.utils.special_sum_set import is_special_sum_set
import math

KNOWN_SETS = {
    1: {1},
    2: {1, 2},
    3: {2, 3, 4},
    4: {3, 5, 6, 7},
    5: {6, 9, 11, 12, 13},
    6: {11, 18, 19, 20, 22, 25},
}

def calculate_next_special_sum_set(s):
    first = sorted(s)[math.floor(len(s) / 2)]
    return {first} | {first + x for x in s}

N = 7
SUM_OPTIMUM_SET_FOR_N_MINUS_1 = sum(KNOWN_SETS[N - 1])

# The maximum element in the optimum set is assumed to be up to 5 more than the maximum element in the set that the algorithm created
SAFETY_FACTOR = 5

def solve():
    """
    This challange is very weird, but I solved it by using their algorithm and hueristicly verifying that this was the
    optimum set.
    It takes some time to verify, but it works (it can be improved using the solution of problem 106).
    """
    best_set_found = calculate_next_special_sum_set(KNOWN_SETS[N - 1])
    best_sum_found = sum(best_set_found)
    # We assume that the minimal element will be at least the minimum value of the set that the algorithm created
    start = 1
    end = start + N
    numbers_until_now = list(range(start, end))
    for number in range(max(numbers_until_now) + 1, max(best_set_found) + SAFETY_FACTOR + 1):
        for current_set in combinations(numbers_until_now, N - 1):
            current_set = set(current_set) | {number}
            sum_current_set = sum(current_set)
            if sum_current_set >= best_sum_found or sum_current_set <= SUM_OPTIMUM_SET_FOR_N_MINUS_1:
                continue
            if is_special_sum_set(current_set):
                if sum_current_set < best_sum_found:
                    best_set_found = current_set
                    best_sum_found = sum(best_set_found)
        numbers_until_now.append(number)
    return ''.join(map(str, sorted(best_set_found)))

def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
