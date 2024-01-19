"""
Challenge 63 of project euler - Powerful Digit Counts

@author Ori Dabush
"""

from itertools import count


X_MIN, X_MAX = 2, 9
N_MIN = 1


def number_of_digits(number: int) -> int:
    return len(str(number))


def solve():
    """
    We need to find the number of pairs (x, n) where x**n has n digits. That condition holds only if:
    ceil(log10(x ** n)) == n <=> ceil(n * log10(x)) == n <=> ceil(log10(x)) == 1 <=> x is in (1, 10].
    So we can iterate on n's value until x**n has less than n digits and that's it
    (it is enough because if the power will be raised by 1 where the base is in (1, 10] the number of digits of the
    result will be incremented by at most 1).
    In addition, 10**n will always have n+1 digits so the condition will never hold for it.
    Another x value we should consider is 1, which for every n the condition will be held.
    """
    result = 1
    for x in range(X_MIN, X_MAX + 1):
        for n in count(start=N_MIN):
            if number_of_digits(x ** n) < n:
                break
            elif number_of_digits(x ** n) == n:
                result += 1
    return result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
