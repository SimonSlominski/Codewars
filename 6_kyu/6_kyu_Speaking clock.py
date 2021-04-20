""" All tasks come from www.codewars.com """

"""
TASK: Speaking clock

For a simple watch face we want the current time spelled out in english. 
Write a function get_time_text(cls, h, m) that takes the time as two integers
and returns the spelled out time as written below.

We would like the text to be simple to read, so we will round the current time to the next full 5 minutes 
(Definitely more convenient for the user than rounding down...). 
We will use a 12-hour clock (e.g. 13:00 is "one". For this particular clock we will not use "AM" and "PM", 
just the time (and let the user guess which half of the day it is ;-) )

The time will be passed in a 24-hour format, and may contain (0, 0) as well as (24, 0).
"""

from math import ceil


NUMS = ["midnight", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen",
        "twenty", "twenty one", "twenty two",
        "twenty three", "twenty four",
        "twenty-five", "twenty six", "twenty seven",
        "twenty eight", "twenty nine"]


class WorldClock(object):

    @classmethod
    def get_time_text(cls, h, m):

        m = ceil(m / 5.0) * 5

        # Midnight
        if h == 0 and m == 0:
            return f"midnight"
        elif h == 24 and m == 0:
            return f"midnight"
        elif h == 23 and m == 60:
            return f"midnight"
        elif h == 24:
            return f"{NUMS[m]} past midnight"
        elif h == 23:
            return f"{NUMS[m]} to midnight"

        # Noon
        if h == 12 and m == 0:
            return f"noon"
        elif h == 11 and m == 60:
            return f"noon"
        elif h == 12 and m == 15:
            return f"quarter past noon"
        elif h == 12 and m < 30:
            return f"{NUMS[m]} past noon"
        elif h == 11 and m > 30:
            return f"{NUMS[m]} to noon"

        # o'clock
        elif m == 0:
            return f"{NUMS[h % 12]}"

        # Quarters
        elif m == 15:
            return f"quarter past {NUMS[h]}"
        elif m == 45:
            return f"quarter to {NUMS[h + 1]}"

        # Half
        elif m == 30:
            return f"half past {NUMS[h]}"

        # To
        elif m >= 30:
            print(m)
            return f"{NUMS[60 - m]} to {NUMS[(h % 12) + 1]}"

        # Past
        elif m <= 30:
            return f"{NUMS[m]} past {NUMS[h]}"


if __name__ == '__main__':
    print(WorldClock.get_time_text(5, 0))      # "five"
    print(WorldClock.get_time_text(9, 30))     # "half past nine"
    print(WorldClock.get_time_text(14, 00))    # "two"
    print(WorldClock.get_time_text(15, 46))    # "ten to four"
    print(WorldClock.get_time_text(0, 0))      # "midnight"
    print(WorldClock.get_time_text(24, 0))     # "midnight"
