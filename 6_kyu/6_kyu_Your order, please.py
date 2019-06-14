""" All tasks come from www.codewars.com """

"""
TASK: Your order, please

Your task is to sort a given string. Each word in the string will contain a single number. 
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. 
The words in the input String will only contain valid consecutive numbers.

Examples:
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""

def order(sentence):
    words = sentence.split()

    result = ""

    words_dict = {"1":"NONE", "2":"NONE", "3":"NONE", "4":"NONE", "5":"NONE", "6":"NONE", "7":"NONE", "8":"NONE", "9":"NONE", }

    for word in words:
        for char in word:
            if(char.isdigit() and int(char) <= 9):
                words_dict[char] = word

    sorted_dict = sorted(words_dict.items())

    for s in sorted_dict:
        if (s[1] != "NONE"):
            result += s[1] + " "

    result = result[:-1]
    return result

