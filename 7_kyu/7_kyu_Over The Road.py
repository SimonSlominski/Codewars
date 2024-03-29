""" All tasks come from www.codewars.com """

"""
Task
You've just moved into a perfectly straight street with exactly n identical houses on either side of the road. 
Naturally, you would like to find out the house number of the people on the other side of the street. 
The street looks something like this:

Street
1|   |6
3|   |4
5|   |2

Evens increase on the right; odds decrease on the left. House numbers start at 1 and increase without gaps. 
When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2.
"""

def over_the_road(address, n):
    return range(1, n*2+1)[-address]


# print(over_the_road(1, 3)) #6
# print(over_the_road(3, 5)) #8
