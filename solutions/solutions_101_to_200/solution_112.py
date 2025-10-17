"""
Challenge 112 of project euler - Bouncy Numbers

@author Ori Dabush
"""

import math


def is_bouncy(n):
    if n < 100:
        return False
    is_increasing = True
    is_decreasing = True
    for c, next_c in zip(str(n), str(n)[1:]):
        is_increasing = is_increasing and c <= next_c
        is_decreasing = is_decreasing and c >= next_c
        if (not is_decreasing) and (not is_increasing):
            return True
    return (not is_decreasing) and (not is_increasing)


TARGET_PERCENTAGE = 99


def solve():
    current_number = 1
    bouncy_numbers = 0
    while True:
        num_digits = math.ceil(math.log10(current_number))
        # We can optimize this search by skipping groups of numbers with a bouncy prefix
        # Try all prefixes (of length at least 3)
        # For example, for 12000 we will try [120, 1200, 12000] and succeed on 120 so we will skip 100 numbers here 
        for n in range(num_digits - 3, -1, -1):
            group_size = 10 ** n
            group_prefix = current_number // group_size
            if is_bouncy(group_prefix):
                # Check if we passed the target percentage
                if (bouncy_numbers + group_size) / (current_number + group_size) >= TARGET_PERCENTAGE / 100 :
                    # If so, find the first one that passes it
                    # Note: I could do it smarter, but it works fast enough and I don't really need it to be faster
                    for _ in range(group_size):
                        bouncy_numbers += 1
                        if bouncy_numbers / current_number >= TARGET_PERCENTAGE / 100:
                            return current_number
                        current_number += 1
                    raise Exception("wtf?")
                else:
                    current_number += group_size
                    bouncy_numbers += group_size
                break
        else:
            current_number += 1


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
