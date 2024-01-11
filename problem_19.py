"""
Challenge 19 of project euler - Counting Sundays

@author Ori Dabush
"""

from utils.dates import number_of_days_in_month, number_of_days_in_year, MONTHS_IN_YEAR, DAYS_IN_WEEK, Days


FIRST_DAY_OF_1900 = Days.MONDAY
START_YEAR, END_YEAR = 1901, 2000
WANTED_DAY = Days.SUNDAY


def solve():
    # The day at January 1st 1901
    current_day = FIRST_DAY_OF_1900 + number_of_days_in_year(1900)
    result = 0
    for year in range(START_YEAR, END_YEAR + 1):
        for month in range(1, MONTHS_IN_YEAR + 1):
            if current_day == WANTED_DAY:
                result += 1
            current_day = Days((current_day + number_of_days_in_month(month, year)) % DAYS_IN_WEEK)
    return result


def main():
    print(f'The answer is {solve()}')


if __name__ == '__main__':
    main()
