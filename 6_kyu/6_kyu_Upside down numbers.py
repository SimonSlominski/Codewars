""" All tasks come from www.codewars.com """

"""
TASK: Upside down numbers

Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down), these numbers remain the same. 
To clarify, if we write them down on a paper and turn the paper upside down, the numbers will be the same. 
Try it and see! Some numbers such as 2 or 5 don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range. 
For example, solve(0,10) = 3, because there are only 3 upside down numbers >= 0 and < 10. They are 0, 1, 8.
"""

"""
Define a function solve that takes two integer arguments: x and y.
Initialize a variable count to 0 to keep track of the number of upside-down numbers.
Iterate through the numbers in the range from x to y, inclusive.
For each number, check if it is an upside-down number by calling the is_upsidedown function.
If the number is an upside-down number, increment the count variable.
After iterating through all the numbers, return the count variable.
"""

def solve(x, y):
    nums = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
    tot = 0
    for i in range(x, y):
        i = str(i)
        m = "".join([nums[x] for x in i[::-1] if x in nums])
        if i == m:
            tot += 1
    return tot
