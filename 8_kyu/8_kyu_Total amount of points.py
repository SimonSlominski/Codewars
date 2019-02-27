""" All tasks come from www.codewars.com """

"""
TASK: Total amount of points

Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

For example: ["3:1", "2:2", "0:1", ...]

Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

if x>y - 3 points
if x<y - 0 point
if x=y - 1 point
Notes:

there are 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
"""

def points(games):
    score = 0

    for i in games:
        if i[0] > i[2]:
            score += 3
        elif i[0] == i[2]:
            score += 1
    return score

