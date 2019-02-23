""" All tasks come from www.codewars.com """

"""
TASK: Unlucky Days

Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.

Find the number of Friday 13th in the given year.

Input: Year as an integer.

Output: Number of Black Fridays in the year as an integer.

Examples:
unlucky_days(2015) == 3
unlucky_days(1986) == 1

"""

from datetime import date, timedelta


def unlucky_days(year):
    day = date(year, 1, 1)
    end = date(year, 12, 31)
    one_day = timedelta(days=1)
    counter = 0

    while day < end:
        if day.weekday() == 4 and day.day == 13:
            counter += 1
        day += one_day

    return counter
