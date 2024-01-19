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
    We need to find the number of pairs (x, n) where x**n has n digits.
    For every x >= 10, increasing n by one means adding at least one digit because it multiplies the number by x
    which is greater or equal to 10. Because in the first place the number of digits is greater than n (there are at
    least 2 digits when n = 1), the number of digits will always be greater than n.

    We left with x can be only in the range [1, 9]. we can iterate on n until the number of digits is less than n,
    because from that point and on the number of digits will always be less than n similarly to before (increasing n
    by one means adding at most one digit because it multiplies by a number less than 10).

    1 is special because for every n the result will be 1 and the loop won't stop, so we can consider it as only 1
    number by initializing the counter to 1.
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
