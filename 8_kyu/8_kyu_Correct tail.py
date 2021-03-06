""" All tasks come from www.codewars.com """

"""
TASK: Correct tail

Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps
the animals do not have the right tails. To help her, you must correct the broken function to make sure
that the second argument (tail), is the same as the last letter of the first argument (body) 
- otherwise the tail wouldn't fit!

If the tail is right return true, else return false.
The arguments will always be strings, and normal letters.

assert_equals(correct_tail("Fox", "x"), True)
assert_equals(correct_tail("Giraffe", "d"), False)
"""

def correct_tail(body, tail):
    return body[-1] == tail[0]

