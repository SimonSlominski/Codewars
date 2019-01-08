""" All tasks come from www.codewars.com """

"""
TASK: Write Number in Expanded Form - Part 2

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(1.24) # Should return '1 + 2/10 + 4/100'
expanded_form(7.304) # Should return '7 + 3/10 + 4/1000'
expanded_form(0.04) # Should return '4/100'
"""


def expanded_form(num):
    n = str(num)
    dot_index = n.index('.')
    length = len(n) - dot_index - 1
    numbers = n[:dot_index] + n[dot_index + 1:]

    first_result = ' + '.join(numbers[i] + (dot_index-i-1) * '0' for i in range(dot_index) if numbers[i] != '0')
    second_result = ' + '.join(numbers[i+dot_index] + '/1' + (i+1) * '0' for i in range(length) if numbers[i+dot_index] != '0')

    return second_result if not first_result else first_result + ' + ' + second_result



# TESTS:
print(expanded_form(1.24))
print(expanded_form(7.304))
print(expanded_form(0.04))
print(expanded_form(90.456))
print(expanded_form(74.001))

