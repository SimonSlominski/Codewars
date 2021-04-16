""" All tasks come from www.codewars.com """

"""
TASK: Read the time

Given time in 24-hour format, convert it to words. For example:
13:00 = one o'clock 
13:09 = nine minutes past one 
13:15 = quarter past one 
13:29 = twenty nine minutes past one
13:30 = half past one 
13:31 = twenty nine minutes to two
13:45 = quarter to two 
00:48 = twelve minutes to one
00:08 = eight minutes past midnight
12:00 = twelve o'clock
00:00 = midnight

Note: If minutes == 0, use 'o'clock'. 
      If minutes <= 30, use 'past', 
      If minutes > 30, use 'to'.
"""

NUMS = ["midnight", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen",
        "twenty", "twenty one", "twenty two",
        "twenty three", "twenty four",
        "twenty five", "twenty six", "twenty seven",
        "twenty eight", "twenty nine"]

def solve(time):
    h, m = time.split(":")
    h, m = int(h), int(m)
    if h >= 12 and h < 23:
        h %= 12

    if h == 0 and m == 0:
        return f"midnight"

    elif h ==23 and m == 0:
        return f"{NUMS[h % 12]} o'clock"

    elif m == 0:
        return f"{NUMS[h]} o'clock"

    elif m == 1:
        return f"one minute past {NUMS[h]}"

    elif h == 23 and m == 59:
        return  f"one minute to {NUMS[(h + 1) % 12]}"

    elif m == 59:
        return f"one minute to {NUMS[h + 1]}"

    elif h == 23 and m == 15:
        return f"quarter past {NUMS[h % 12]}"

    elif m == 15:
        return f"quarter past {NUMS[h]}"

    elif m == 30:
        return f"half past {NUMS[h]}"

    elif h == 23 and m == 45:
        return f"quarter to {NUMS[(h + 1) % 12]}"

    elif m == 45:
        return f"quarter to {NUMS[h + 1]}"

    elif m <= 30:
        return f"{NUMS[m]} minutes past {NUMS[h]}"

    elif h == 23 and m > 30:
        return f"{NUMS[60 - m]} minutes to {NUMS[(h + 1) % 12]}"

    elif m > 30:
        return f"{NUMS[60 - m]} minutes to {NUMS[h + 1]}"

if __name__ == '__main__':
    print(solve("13:00")) # "one o'clock
    print(solve("13:09")) # "nine minutes past one"
    print(solve("12:00")) # "twelve o'clock"
    print(solve("00:00")) # "midnight"
    print(solve("00:01")) # "one minute past midnight"
    print(solve("23:31")) # "twenty nine minutes to midnight"
    print(solve("11:31")) # "twenty nine minutes to twelve"
    print(solve("23:59")) # "one minute to midnight"
    print(solve("11:59")) # "one minute to twelve"




