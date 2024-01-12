"""
Challenge 39 of project euler - Integer Right Triangles

@author Ori Dabush
"""

UPPER_LIMIT = 1000


def find_number_of_solutions(perimeter: int) -> int:
    count = 0
    for a in range(1, perimeter):
        """
        We can iterate until '(p - a) / 2' because 'c' > 'a', we also assume 'b' < 'a' 
        so we run until 'min(a, (p - a) / 2)'
        """
        for b in range(1, min(a, (perimeter - a) // 2)):
            c = (a ** 2 + b ** 2) ** 0.5
            # If c is not an integer continue
            if c != float(int(c)):
                continue
            if a + b + c == perimeter:
                print(perimeter, a, b, c)
                count += 1
    return count


def solve():
    return max(range(1, UPPER_LIMIT + 1), key=find_number_of_solutions)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
