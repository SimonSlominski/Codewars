""" All tasks come from www.codewars.com """

"""
TASK: Separate The Wheat From The Chaff

Given a sequence of n integers , separate the negative numbers (chaff) from positive ones (wheat).

Notes
Sequence size is at least 3
Return a new sequence, such that negative numbers (chaff) come first, then positive ones (wheat).
Have no fear , it is guaranteed that there will be no zeroes .!alt
Repetition of numbers in the input sequence could occur , so duplications are included when separating.
If a misplaced positive number is found in the front part of the sequence, 
replace it with the last misplaced negative number (the one found near the end of the input). 
The second misplaced positive number should be swapped with the second last misplaced negative number. 
Negative numbers found at the head (begining) of the sequence, should be kept in place .
"""


def wheat_from_chaff(values):
    number_of_chaff = list(map(lambda x: x < 0, values)).count(True)
    chaff = values[:number_of_chaff]
    wheat = values[number_of_chaff:]
    switchable_chaff = [i for i, x in enumerate(wheat) if x < 0][::-1]
    for i, num in enumerate(chaff):
        if num > 0:
            chaff[i] = wheat[switchable_chaff[0]]
            wheat[switchable_chaff[0]] = num
            del switchable_chaff[0]
    return chaff + wheat

# Interesting solution
# def wheat_from_chaff(values):
#     v, i, j = values[:], 0, len(values) - 1
#
#     while (i < j):
#         if v[i] < 0:
#             i += 1
#         elif v[j] > 0:
#             j -= 1
#         else:
#             v[i], v[j] = v[j], v[i]
#     return v

# Tests
print(wheat_from_chaff([2,-6,-4,1,-8,-2])) # [-2,-6,-4,-8,1,2]
