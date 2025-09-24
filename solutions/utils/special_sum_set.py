import math
from solutions.utils.subsets import powerset

def check_first_condition(sum_b, sum_c):
    return sum_b != sum_c

def check_second_condition(sum_b, len_b, sum_c, len_c):
    if len_b > len_c:
        return sum_b > sum_c
    elif len_b < len_c:
        return sum_b < sum_c
    return True

def is_special_sum_set(s):
    s = sorted(s)
    # Check the second condition
    n = math.ceil(len(s) / 2)
    if sum(s[:n]) <= sum(s[-(n-1):]):
        return False
    # Check that the sums of all the subsets are unique
    subset_sums = set()
    for s in powerset(s):
        sum_s = sum(s)
        if sum_s in subset_sums:
            return False
        subset_sums.add(sum_s)
    return True
