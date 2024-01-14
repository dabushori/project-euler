"""
Challenge 58 of project euler - Spiral Primes

@author Ori Dabush
"""

from utils.primes import is_prime


def solve():
    current_size = 3
    number_of_primes = 0
    while True:
        top_right_corner = current_size ** 2
        difference_of_corners = current_size - 1
        # Top right corner
        if is_prime(top_right_corner):
            number_of_primes += 1
        # Top left corner
        if is_prime(top_right_corner - difference_of_corners):
            number_of_primes += 1
        # Bottom left corner
        if is_prime(top_right_corner - 2 * difference_of_corners):
            number_of_primes += 1
        # Bottom right corner
        if is_prime(top_right_corner - 3 * difference_of_corners):
            number_of_primes += 1
        number_of_numbers = 2 * current_size - 1
        ratio = number_of_primes / number_of_numbers
        if ratio < 0.1:
            return current_size
        current_size += 2


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
