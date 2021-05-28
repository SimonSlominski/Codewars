""" All tasks come from www.codewars.com """

"""
TASK: Smallest unused ID

You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!

Therefore you need a method, which returns the smallest unused ID for your next new data item...
"""

def next_id(arr):
    for i in range(len(arr)+1):
        if i not in arr:
            return i


if __name__ == '__main__':
    print(next_id([5, 4, 3, 2, 1]))  # 0
    print(next_id([0, 1, 2, 3, 5]))  # 4
    print(next_id([0, 0, 0, 0, 0, 0]))  # 1
    print(next_id([0,1,2,3,4,5,6,7,8,9,10])) # 11
    print(next_id([])) # 0
    print(next_id([0,0,1,1,2,2])) # 3
