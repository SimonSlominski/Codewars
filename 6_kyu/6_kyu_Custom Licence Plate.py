""" All tasks come from www.codewars.com """

"""
TASK: Custom Licence Plate

Task
Implement a function that accepts an ascii input string, and returns the number plate if possible.
You have to replace all special characters and spaces with dashes 
(consecutive characters should be replaced with a single dash), 
and truncate the result to maximum 8 characters (if longer). 
If the result complies with the above criteria, return it capitalized; otherwise return "not possible".

Examples
"mercedes"    -->  "MERCEDES"
"anter69"     -->  "ANTER-69"
"1st"         -->  "1-ST"
"~c0d3w4rs~"  -->  "C-0-D-3"
"I'm cool!"   -->  "I-M-COOL"
"1337"        -->  "not possible"
"""

import re


def licence_plate(s):
    plate = '-'.join(re.findall(r'[A-Z]+|\d+', s.upper()))[:8].rstrip('-')

    if len(plate) > 1 and not plate.isdigit():
        return plate
    else:
        return f"not possible"
