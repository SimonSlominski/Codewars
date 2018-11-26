""" All tasks come from www.codewars.com """

"""
TASK: Sort the odd

Your task is to sort ascending odd numbers but even numbers must be on their places.
Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example:
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
"""

def sort_array(source_array):

    odd_numbers = sorted([num for num in source_array if num % 2 != 0])  # Output: sorted list with only odd numbers
    odd_int = 0     # Variable needed to index numbers in 'odd_numbers'
    result = []     # Empty list to hold the result

    for i in source_array:
        if i % 2 != 0:
            result.append(odd_numbers[odd_int])     # If 'i' is an odd number --> add first number from 'odd_numbers'
            odd_int += 1                            # Increasing index by 1 for the next loop
        else:
            result.append(i)                        # If 'i' is even add that number to 'result'
    return result
