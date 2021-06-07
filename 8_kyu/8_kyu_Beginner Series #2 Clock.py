""" All tasks come from www.codewars.com """

"""
TASK: Beginner Series #2 Clock

Clock shows h hours, m minutes and s seconds after midnight.
Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
"""


HOUR_TO_MS = 3600000
MIN_TO_MS = 60000
SEC_TO_MS = 1000

def past(h, m, s):
    return h*HOUR_TO_MS + m*MIN_TO_MS + s*SEC_TO_MS
