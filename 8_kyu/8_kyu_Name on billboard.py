""" All tasks come from www.codewars.com """

"""
TASK: Name on billboard

You can print your name on a billboard ad. Find out how much it will cost you. 
Each letter has a default price of £30, but that can be different if you are given 2 parameters instead of 1.

You can not use multiplier "*" operator.

If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 leters * 30 = 600 (Space counts as a letter).
"""


def billboard(name, price=30):
    return sum(price for letter in name)


def billboard(name, price=30):
    counter = 0
    cost = 0
    while counter < len(name):
        cost += price
        counter += 1
    return cost

