#!/usr/bin/python
import sys
import re
import unittest
import string
#Takes in a string or strings
def add(numbers):
    result = 0
    delim = ','
    if numbers[:2] == '//':
        if numbers[2] in string.punctuation:
            delim = '\\' + numbers[2]
        else:
            delim = numbers[2]
    endl = re.compile('{0}|\n'.format(delim))
    for number in re.split(endl,numbers):
        if '-' in number:
            matches = re.findall('-\d*', numbers)
            errorString = "Negatives not allowed: "
            for negative in matches:
                errorString += negative +','
            raise ValueError(errorString)
        if number.isdigit():
            result += int(number)
    return result

