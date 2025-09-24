"""
Challenge 103 of project euler - Special Subset Sums: Optimum

@author Ori Dabush
"""

from itertools import chain, combinations, count

KNOWN_SETS = {
    1: {1},
    2: {1, 2},
    3: {2, 3, 4},
    4: {3, 5, 6, 7},
    5: {6, 9, 11, 12, 13},
    6: {11, 18, 19, 20, 22, 25},
}

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def check_first_condition(b, c):
    return sum(b) != sum(c)

def check_second_condition(b, c):
    if len(b) > len(c):
        return sum(b) > sum(c)
    elif len(b) < len(c):
        return sum(b) < sum(c)
    return True

def is_special_sum_set(s):
    current_subsets = list(powerset(s))
    for b in list(powerset(s)):
        for c in current_subsets:
            if 0 in (len(b), len(c)) or (set(b) & set(c)):
                continue
            if not check_first_condition(b, c) or not check_second_condition(b, c):
                return False
        current_subsets.remove(b)
    return True

N = 6

def solve():
    numbers_until_now = list(range(1, 13))
    for number in count(start=max(numbers_until_now) + 1):
        # print(f'{numbers_until_now = }')
        for current_set in combinations(numbers_until_now, N - 1):
            current_set = sorted(set(current_set) | {number})
            if is_special_sum_set(current_set):
                return ''.join(str(n) for n in current_set)
        numbers_until_now.append(number)



def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
