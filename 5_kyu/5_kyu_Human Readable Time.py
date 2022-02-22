""" All tasks come from www.codewars.com """

"""
TASK: Human Readable Time

Write a function, which takes a non-negative integer (seconds) as input 
and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
"""

def make_readable(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    return "%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60)

# Shorter version
# def make_readable(seconds):
#     return '{:02}:{:02}:{:02}'.format(seconds / 3600, seconds / 60 % 60, seconds % 60)

# Tests zone
print(make_readable(0)) #, "00:00:00")
print(make_readable(5)) #, "00:00:05")
print(make_readable(60)) #, "00:01:00")
print(make_readable(86399)) #, "23:59:59")
print(make_readable(359999)) #, "99:59:59")
