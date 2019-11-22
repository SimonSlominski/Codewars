""" All tasks come from www.codewars.com """

"""
TASK: Who has the most money?

You're going on a trip with some students and it's up to you to keep track of how much money each Student has. 
A student is defined like this:

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
As you can tell, each Student has some fives, tens, and twenties. 
Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".

Notes:
Each student will have a unique name
There will always be a clear winner: either one person has the most, or everyone has the same amount
If there is only one student, then that student has the most money
"""


class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students):
    if len(students) == 1:
        return students[0].name

    cash_balance = (students[0].fives * 5) + (students[0].tens * 10) + (students[0].twenties * 20)
    student_name = students[0].name
    equal = 0

    for i in range(len(students)):
        new_cash_balance = (students[i].fives * 5) + (students[i].tens * 10) + (students[i].twenties * 20)
        if new_cash_balance == cash_balance:
            equal += 1
        elif new_cash_balance > cash_balance:
            cash_balance = new_cash_balance
            student_name = students[i].name

    if equal == len(students):
        return 'all'
    else:
        return student_name
