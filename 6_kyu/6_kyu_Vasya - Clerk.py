""" All tasks come from www.codewars.com """

"""
TASK: Vasya - Clerk

The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. 
Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change 
(you can't make two bills of 25 from one of 50)
"""


def tickets(people):
    # If it was a regular cash register, it is better to use a 'dictionary' instead of a 'list'.
    cashbox_25 = 0
    cashbox_50 = 0

    for paid in people:
        # Handle the payment for 25
        if paid == 25:
            cashbox_25 += 1
        # Handle the payment for 50
        if paid == 50:
            cashbox_50 += 1
            if cashbox_25 >= 1:
                cashbox_25 -= 1
            else:
                return "NO"
        # Handle the payment for 100
        if paid == 100:
            # There is no need to add 100 to cashbox
            if cashbox_50 >= 1 and cashbox_25 >= 1:
                cashbox_50 -= 1
                cashbox_25 -= 1
            elif cashbox_50 == 0 and cashbox_25 >= 3:
                cashbox_25 -= 3
            else:
                return "NO"

    return "YES"
