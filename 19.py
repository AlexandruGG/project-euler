# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


from datetime import date
from collections import Counter
from typing import Dict


def total_sundays(start_year: int, end_year: int) -> int:
    counter: Dict[int, int] = Counter()

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            day = date(year, month, 1)
            counter[day.weekday()] += 1

    return counter[6]


print(f"Number of Sundays: {total_sundays(1901, 2000)}")
