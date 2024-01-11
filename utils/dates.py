"""
* Thirty days has September, April, June and November.
* All the rest have thirty-one, Saving February alone, Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
"""

from enum import IntEnum


THIRTY_DAYS = 30
THIRTY_DAYS_MONTHS = [4, 6, 9, 11]
THIRTY_ONE_DAYS = 31
THIRTY_ONE_DAYS_MONTHS = [1, 3, 5, 7, 8, 10, 12]
DAYS_IN_REGULAR_FEBRUARY = 28
DAYS_IN_LEAP_YEAR_FEBRUARY = 29
MONTHS_IN_YEAR = 12
DAYS_IN_WEEK = 7


class Days(IntEnum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


def is_century(year: int) -> bool:
    return year % 100 == 0


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (not is_century(year) or year % 400 == 0)


def number_of_days_in_month(month, year):
    if month in THIRTY_DAYS_MONTHS:
        return THIRTY_DAYS
    if month in THIRTY_ONE_DAYS_MONTHS:
        return THIRTY_ONE_DAYS
    if is_leap_year(year):
        return DAYS_IN_LEAP_YEAR_FEBRUARY
    return DAYS_IN_REGULAR_FEBRUARY


def number_of_days_in_year(year):
    return sum(number_of_days_in_month(month, year) for month in range(1, MONTHS_IN_YEAR + 1))
