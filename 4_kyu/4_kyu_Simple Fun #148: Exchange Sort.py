""" All tasks come from www.codewars.com """

"""
TASK: Simple Fun #148: Exchange Sort

Given a sequence (length ≤ 1000) of 3 different key values (7, 8, 9), 
your task is to find the minimum number of exchange operations necessary to make the sequence sorted.

One operation is the switching of 2 key values in the sequence.

Example:
For sequence = [7, 7, 8, 8, 9, 9], the result should be 0. It's already a sorted sequence.
For sequence = [9, 7, 8, 8, 9, 7], the result should be 1. We can switching sequence[0] and sequence[5].
For sequence = [8, 8, 7, 9, 9, 9, 8, 9, 7], the result should be 4.

 [8, 8, 7, 9, 9, 9, 8, 9, 7] 
 switching sequence[0] and sequence[3]
 --> [9, 8, 7, 8, 9, 9, 8, 9, 7]
 switching sequence[0] and sequence[8]
 --> [7, 8, 7, 8, 9, 9, 8, 9, 9]
 switching sequence[1] and sequence[2]
 --> [7, 7, 8, 8, 9, 9, 8, 9, 9]
 switching sequence[5] and sequence[7]
 --> [7, 7, 8, 8, 8, 9, 9, 9, 9]

So 4 is the minimum number of operations for the sequence to become sorted.

Input/Output
[input] integer array sequence
[output] an integer = the minimum number of operations.
"""


def exchange_sort(sequence):
    sorted_sequence = sorted(sequence)
    swap_counter = 0
    for i in range(0, len(sorted_sequence) - 1):
        if sequence[i] != sorted_sequence[i]:
            for j in range(i + 1, len(sorted_sequence)):
                if sequence[j] == sorted_sequence[i] and sequence[j] != sorted_sequence[j]:
                    swap_counter += 1
                    sequence[i], sequence[j] = sequence[j], sequence[i]
                    for k in range(j + 1, len(sorted_sequence)):
                        if sequence[k] == sorted_sequence[i] and sorted_sequence[k] == sequence[j]:
                            sequence[j], sequence[k] = sequence[k], sequence[j]

                            break
                    break

    return swap_counter

