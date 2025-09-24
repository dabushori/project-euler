"""
Challenge 106 of project euler - Special Subset Sums: Meta-testing

@author Ori Dabush
"""

import math
from functools import cache
from utils.subsets import subsets


N = 12
INDEX_SET = list(range(1, N + 1))


@cache
def compare_subsets(s1, s2):
    """
    This function assumes s1 != s2.
    It returns True or False based on comparison (based on the second rule assumption and on the indexes order)
    and None if it can't determine the comparison result.
    """
    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 == len_s2:
        sorted_zip = list(zip(sorted(s1), sorted(s2)))
        if all(a1 >= a2 for a1, a2 in sorted_zip):
            return True
        elif all(a1 <= a2 for a1, a2 in sorted_zip):
            return True
        else:
            return None
    else:
        return len_s1 > len_s2


def count_subset_pair_to_compare(size):
    """
    Count the subsets pairs of size `size`
    """
    subset_pair_to_compare = 0
    subsets_list = list(subsets(INDEX_SET, size, size))
    for subset1 in subsets_list.copy():
        for subset2 in subsets_list:
            if set(subset1) & set(subset2):
                continue
            comparison_result = compare_subsets(subset1, subset2)
            # Count the number of subsets which are needed to be compared
            if comparison_result is None:
                subset_pair_to_compare += 1
        subsets_list.remove(subset1)
    return subset_pair_to_compare


def solve():
    sets_to_check = 0
    """
    We don't need to test subsets of size:
    * 0, N - there's only one
    * 1 - they are unique
    * [N+1/2, N-1] - they won't be disjoint
    """
    for size in range(2, math.ceil(N / 2) + 1):
        sets_to_check += count_subset_pair_to_compare(size)
    return sets_to_check


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
