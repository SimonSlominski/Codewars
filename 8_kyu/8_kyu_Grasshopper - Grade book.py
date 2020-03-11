""" All tasks come from www.codewars.com """

"""
TASK: Grasshopper - Grade book

Complete the function so that it finds the mean of the three scores passed to it 
and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'

Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
"""


from statistics import mean


GRADE_BOUNDARIES = {
    'A': [90, 100],
    'B': [80, 89],
    'C': [70, 79],
    'D': [60, 69],
    'F': [0, 59],
}


def get_grade(s1, s2, s3):
    average_grade = mean([s1, s2, s3])

    for grade, bounds in GRADE_BOUNDARIES.items():
        if average_grade >= bounds[0] and average_grade <= bounds[1]:
            return grade
