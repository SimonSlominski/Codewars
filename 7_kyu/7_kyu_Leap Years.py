""" All tasks come from www.codewars.com """

"""
TASK: Leap Years

In this kata you should simply determine, whether a given year is a leap year or not. 
In case you don't know the rules, here they are:

years divisible by 4 are leap years
but years divisible by 100 are no leap years
but years divisible by 400 are leap years
"""

def isLeapYear(year):
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0

