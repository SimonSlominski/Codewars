""" All tasks come from www.codewars.com """

"""
TASK: CamelCase Method

Write simple camelCase method for strings. All words must have their first letter capitalized without spaces.

Example:
camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
"""


def camel_case(string):
    return string.title().replace(" ", "")

