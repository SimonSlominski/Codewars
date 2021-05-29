""" All tasks come from www.codewars.com """

"""
TASK: Longest alphabetical substring

Find the longest substring in alphabetical order.

Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
There are tests with strings up to 10 000 characters long so your code will need to be efficient.
The input will only consist of lowercase characters and will be at least one letter long.
"""

def longest(s):
    longest = s[0]
    current = s[0]
    for c in s[1:]:
        if c >= current[-1]:
            current += c
            if len(current) > len(longest):
                longest = current
        else:
            current = c
    return longest


if __name__ == '__main__':
    print(longest('nab'))           # 'ab'
    print(longest('abcdeapbcdef'))  # 'abcde'
    print(longest('asdfaaaabbbbcttavvfffffdf')) # 'aaaabbbbctt'
    print(longest('asdfbyfgiklag')) # 'fgikl'
    print(longest('z'))             # 'z'
    print(longest('zyba'))          # 'z'
