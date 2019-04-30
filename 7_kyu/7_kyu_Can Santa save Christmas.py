""" All tasks come from www.codewars.com """

"""
TASK: Can Santa save Christmas

Can Santa save Christmas?
Oh no! Santa's little elves are sick this year. He has to distribute the presents on his own. 
But he has only 24 hours left. Can he do it?
Your job is to determine if Santa can distribute all the presents in 24 hours. 

Your Task:
You will get an array as input with time durations as string in the following format: 
"hh:mm:ss"

Each duration is a present Santa has to distribute. 

Return true or false whether he can do it in 24 hours or not. 
"""

from datetime import timedelta

def determineTime(arr):
    satans_time = timedelta()
    for time in arr:
        (h, m, s) = time.split(':')
        satans_time += timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    return satans_time < timedelta(hours=24)

