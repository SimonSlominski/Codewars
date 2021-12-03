""" All tasks come from www.codewars.com """

"""
TASK: Row Weights

Several people are standing in a row divided into two teams.
The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.

Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, 
where the first one is the total weight of team 1, and the second one is the total weight of team 2.

Input >> Output Examples
rowWeights([13, 27, 49])  ==>  return (62, 27)
The first element 62 is the total weight of team 1, and the second element 27 is the total weight of team 2.

rowWeights([50, 60, 70, 80])  ==>  return (120, 140)
The first element 120 is the total weight of team 1, and the second element 140 is the total weight of team 2.
"""

def row_weights(array):
    team_1 = 0
    team_2 = 0
    for index, weight in enumerate(array):
        if index % 2 == 0:
            team_1 += weight
        else:
            team_2 += weight
    return (team_1, team_2)

# best practice
# def row_weights(array):
#     return sum(array[::2]), sum(array[1::2])
