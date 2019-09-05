""" All tasks come from www.codewars.com """

"""
TASK: Reverse FizzBuzz

FizzBuzz is often one of the first programming puzzle people learn. Now undo it with reverse FizzBuzz!

Write a function that accepts a string, which will always be a valid section of FizzBuzz. 
Your function must return an array that contains the numbers in order to generate the given section of FizzBuzz.

Notes:
If the sequence can appear multiple times within FizzBuzz, return the numbers that generate the first instance of that sequence.
All numbers in the sequence will be greater than zero.
You will never receive an empty sequence.

Examples
reverse_fizzbuzz("1 2 Fizz 4 Buzz")        -->  [1, 2, 3, 4, 5]
reverse_fizzbuzz("Fizz 688 689 FizzBuzz")  -->  [687, 688, 689, 690]
reverse_fizzbuzz("Fizz Buzz")              -->  [9, 10]
"""


def reverse_fizzbuzz(string):

    if string == "Fizz": return [3]
    if string == "Buzz": return [5]
    if string == "FizzBuzz": return [15]
    if string == "Fizz Buzz": return [9, 10]
    if string == "Buzz Fizz": return [5, 6]

    arr = string.split()
    for index, value in enumerate(arr):
        if value.isnumeric():
            i = int(value) - index
            return [i + k for k in range(len(arr))]

