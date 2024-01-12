"""
Challenge 28 of project euler - Number Spiral Diagonals

@author Ori Dabush
"""

SQUARE_SIZE = 1001


def solve():
    result = 1
    for square_index in range(1, (SQUARE_SIZE - 1) // 2 + 1):
        top_right_corner = (2 * square_index + 1) ** 2
        difference_of_corners = 2 * square_index
        result += sum((
            # Top right corner
            top_right_corner,
            # Top left corner
            top_right_corner - difference_of_corners,
            # Bottom left corner
            top_right_corner - 2 * difference_of_corners,
            # Bottom right corner
            top_right_corner - 3 * difference_of_corners
        ))
    return result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
