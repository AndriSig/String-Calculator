#!/usr/bin/python
import sys
import re
import unittest
import string
#Takes in a string of numbers and gives their sum
def add(numbers):
    result = 0
    delim = ',|\n'
    if numbers[:2] == '//':
        delim = re.compile(findDelim(numbers))
        numbers = re.sub(r'^[^\d]*','', numbers)
    for num in re.split(delim, numbers):
        if '-' in num:
            raiseNeg(numbers)
        if num.isdigit() and int(num) < 1001:
            result += int(num)
    return result
 #Takes in a string of numbers and gives the delimiter/s at the start of said string 
def findDelim(input):
    input = re.findall(r'^[^\d]*', input)[0]
    if re.match(r'//(\[.*?\])', input) is not None:
        delim = re.findall(r'\[([^]]*)\]', input)
        if len(delim) > 1:
            combo = '['
            for d in delim:
                combo += '(' + re.escape(d) + ')'
            combo += ']'
            return combo
        else:
            return re.escape(delim[0])
    else:
        return re.escape(input[2])
#Raises an exception if called
def raiseNeg(numbers):
    matches = re.findall('-\d*', numbers)
    errorString = "Negatives not allowed: "
    for negative in matches:
        errorString += negative +','
    raise ValueError(errorString)
