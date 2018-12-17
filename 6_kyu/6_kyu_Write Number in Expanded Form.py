""" All tasks come from www.codewars.com """

"""
TASK: Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

Example:
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""

# Newbie style
def expanded_form(n):
    result_list = []
    for num in str(n):
        result_list.append(num)

    result = ''

    for index, value in zip(range(len(result_list) - 1, -1, -1), result_list):
        if int(value) != 0:
            result += value + '0' * index + ' ' + '+ '
    return result[:-3]


# More Pythonic style
def expanded_form_pro(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

