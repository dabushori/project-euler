"""
Challenge 44 of project euler - Pentagon Numbers

@author Ori Dabush
"""

from solutions.utils.pentagons import get_pentagon_number, get_pentagon_numbers, is_pentagon_number


def solve():
    """
    By iterating on the difference we make sure that the first option we find is the one with the minimal difference.
    We can stop iterating on p_j once p_k is smaller than p_(j+1), because the differences keeps getting bigger
    so all the next pentagon numbers will also be less than p_(j+1).
    Also, we can optimize number of iterations by making sure p_j <= d because if p_j > d it will be found when
    d will be equal to p_j.
    """
    for d in get_pentagon_numbers():
        for j, p_j in get_pentagon_numbers(indexed=True):
            p_k = p_j + d
            if p_j > d or p_k < get_pentagon_number(j + 1):
                break
            if is_pentagon_number(p_k) and is_pentagon_number(p_j + p_k):
                return d


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
