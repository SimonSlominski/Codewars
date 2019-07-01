""" All tasks come from www.codewars.com """

"""
TASK: Capitals first!

Create a function that takes an input String and returns a String, where all the uppercase words 
of the input String are in front and all the lowercase words at the end. 
The order of the uppercase and lowercase words should be the order in which they occur.

If a word starts with a number or special character, skip the word and leave it out of the result.

Input String will not be empty.

Example:
"hey You, Sort me Already!" --> "You, Sort Already! hey me"
"""


def capitals_first(text):
    upper_words = ' '.join([word for word in text.split() if word[0].isupper()])
    lower_words = ' '.join(word for word in text.split() if word[0].islower())

    if upper_words and lower_words:
        return upper_words + " " + lower_words
    elif upper_words and not lower_words:
        return upper_words
    else:
        return lower_words

