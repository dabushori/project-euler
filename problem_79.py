"""
Challenge 79 of project euler - Passcode Derivation

@author Ori Dabush
"""

from utils.inputs import get_input


def get_relations(attempts: list[str]) -> set[tuple[str, str]]:
    """
    Find all the relations between digits
    """
    digits = ''.join(set(''.join(attempts)))
    relations = []
    # Get the relations given by the attempts
    for x, y, z in attempts:
        relations.extend([(x, y), (y, z), (x, z)])
    relations_dict = {
        digit: {y for x, y in relations if x == digit}
        for digit in digits
    }
    # Expand it recursively to multiple-hop relations
    for digit in digits:
        current_digits = relations_dict[digit] - {digit}
        while current_digits:
            current_digit = current_digits.pop()
            if relations_dict[current_digit] <= relations_dict[digit]:
                break
            relations_dict[digit].update(relations_dict[current_digit])
            current_digit = relations_dict[current_digit]
    return [(x, y) for x in relations_dict for y in relations_dict[x]]


def solve():
    attempts = get_input(79).split()
    relations = get_relations(attempts)
    result = ''
    """
    In each iteration get the digit that is bigger then the minimal number of digits, 
    append all the digits which are smaller than it and then append the digits itself and 
    remove all the relations which it appears as the bigger digit.
    """
    while relations:
        digit = min(relations, key=lambda n: len([_ for _, y in relations if y == n[1]]))[1]
        smaller_digits = [x for x, y in relations if y == digit if x not in result]
        result = result + ''.join(smaller_digits) + digit
        relations = [(x, y) for x, y in relations if y != digit]
        print(result)


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
