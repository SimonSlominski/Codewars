""" All tasks come from www.codewars.com """

"""
TASK: Please help Bob

Description
In English we often use "neutral vowel sounds" such as "umm", "err", "ahh" 
as fillers in conversations to help them run smoothly.

Bob always finds himself saying "err". Infact he adds an "err" to every single word he says that ends in a consonant! 
Because Bob is odd, he likes to stick to this habit even when emailing.


Task
Bob is begging you to write a function that adds "err" to the end of every word whose last letter is a consonant 
(not a vowel, y counts as a consonant).

The input is a string that can contain upper and lowercase characters, some punctuation but no numbers. 
The solution should be returned as a string.

NOTE: If the word ends with an uppercase consonant, the following "err" will be uppercase --> "ERR".

eg:
"Hello, I am Mr Bob" --> "Hello, I amerr Mrerr Boberr"
"THIS IS CRAZY!"  --> "THISERR ISERR CRAZYERR!"
"""


def err_bob(string):
    t, a = "", "aeioubcdfghjklmnpqrstvwxyz"
    for i, c in enumerate(string + " "):
        if c.lower() not in a and string[i - 1].lower() in a[5:]:
            t += "ERR" if string[i - 1].isupper() else "err"
        t += c
    return t[:-1]

