""" All tasks come from www.codewars.com """

"""
TASK: Matching And Substituting

I got lots of files beginning like this:

Program title: Primes
Author: Kern
Corporation: Gold
Phone: +1-503-555-0091
Date: Tues April 9, 2005
Version: 6.7
Level: Alpha

The function change(s, prog, version) given:
s=data, prog="Ladder" , version="1.1" will return:
"Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.1"

Rules:
1) The date should always be "2019-01-01".
2) The author should always be "g964".
3) Replace the current "Program Title" with the prog argument supplied to your function. 
   Also remove "Title", so in the example case "Program Title: Primes" becomes "Program: Ladder".
4) Remove the lines containing "Corporation" and "Level" completely.
5) Phone numbers and versions must be in valid formats.
6) A valid version in the given string data is one or more digits followed by a dot, followed by one or more digits. 
   So 0.6, 5.4, 14.275 and 1.99 are all valid, but versions like .6, 5, 14.2.7 and 1.9.9 are invalid.
7) A valid phone format is +1-xxx-xxx-xxxx, where each x is a digit.
8) If the phone or version format is not valid, return "ERROR: VERSION or PHONE".
9) If the version format is valid and the version is anything other than 2.0, 
   replace it with the version parameter supplied to your function. If it’s 2.0, don’t modify it.
10)If the phone number is valid, replace it with "+1-503-555-0090".
"""

import re

def change(s, prog, version):

    # Clean data
    data = s.split('\n')

    # Data to return
    data_program = prog
    data_author = 'g964'
    data_phone = '+1-503-555-0090'
    data_date = '2019-01-01'
    data_version = version

    # Data for validation
    data_string_version = data[5].split(' ')
    data_string_phone = data[3].split(' ')

    # Validation
    data_phone_validation = re.compile('^(\+1)-\d{3}-\d{3}-\d{4}$')
    data_version_validation = re.compile('^(\d{1,}).(\d{1,})$')


    if not data_phone_validation.match(data_string_phone[1]) or not data_version_validation.match(data_string_version[1]):
         return "ERROR: VERSION or PHONE"
    elif data_phone_validation.match(data_string_phone[1]) and data_version_validation.match(data_string_version[1]) and data_string_version[1] == '2.0':
        return f"Program: {data_program} Author: {data_author} Phone: {data_phone} Date: {data_date} Version: {data_string_version[1]}"
    else:
        return f"Program: {data_program} Author: {data_author} Phone: {data_phone} Date: {data_date} Version: {data_version}"



# Tests examples
s1 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-0091\nDate: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha'
s11 = 'Program title: Hammer\nAuthor: Tolkien\nCorporation: IB\nPhone: +1-503-555-0090\nDate: Tues March 29, 2017\nVersion: 2.0\nLevel: Release'
s12 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-0095\nDate: Tues April 9, 2005\nVersion: 6\nLevel: Alpha'

print(change(s1, 'Ladder', '1.1'))      # Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.1
print(change(s11, 'Balance', '1.5.6'))  # Program: Balance Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 2.0)
print(change(s12, 'Ladder', '1.1'))     # ERROR: VERSION or PHONE

