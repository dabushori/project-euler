"""
Challenge 93 of project euler - Arithmetic Expressions

@author Ori Dabush
"""

from itertools import permutations, product, count


OPS = {'+', '-', '*', '/'}
TEMPLATES = {
    # ((a op b) op c) op d
    '(({}{}{}){}{}){}{}',
    # (a op (b op c)) op d
    '({}{}({}{}{})){}{}',
    # a op ((b op c) op d)
    '{}{}(({}{}{}){}{})',
    # a op (b op (c op d))
    '{}{}({}{}({}{}{}))',
    # (a op b) op (c op d)
    '({}{}{}){}({}{}{})',
}
DIGITS = set(range(10))


def highest_number_expressible(a: int, b: int, c: int, d: int) -> int:
    """
    Return the highest number expressible by 'a, b, c, d'.
    The calculation is done by pre-calculating the possible order of operations, and then brute forcing the operators 
    and permutations of 'a, b, c, d' and calculate the expressions that are created by assigning them there.
    """
    expressible_numbers = set()
    for w, x, y, z in permutations([a, b, c, d]):
        for op1, op2, op3 in product(OPS, repeat=3):
            for template in TEMPLATES:
                expression = template.format(w, op1, x, op2, y, op3, z)
                try:
                    result = eval(expression)
                except ZeroDivisionError:
                    continue
                expressible_numbers.add(result)
    # Find the first number starting from 1 that can't be expressible by 'a, b, c, d', and return it minus one
    for n in count(start=1):
        if n not in expressible_numbers:
            return n - 1


def solve():
    # Find the '0 <= a < b < c < d <= 9' which the longest set of consecutive positive integers 1 to n can be obtained.
    return ''.join(str(digit) for digit in max(
        ((a, b, c, d) for d in DIGITS for c in range(d) for b in range(c) for a in range(b)),
        key=lambda args: highest_number_expressible(*args)
    ))


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
