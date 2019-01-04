""" All tasks come from www.codewars.com """

"""
TASK: Simple Fun #79: Delete a Digit

Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example:
For n = 152, the output should be 52;
For n = 1001, the output should be 101.
For n = 10, the 

Input/Output
[input] integer n
[output] an integer

Constraints: 10 ≤ n ≤ 1000000.

"""


def delete_digit(n):
    numbers = list(str(n))

    if len(numbers) == 2:
        return int(max(numbers))
    else:
        for i in range(len(numbers)):
            if numbers[i] < numbers[i+1]:
                numbers.remove(numbers[i])
                return int("".join(list(map(str, numbers))))

