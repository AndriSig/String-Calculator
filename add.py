#!/usr/bin/python
import sys
import re
import unittest
import string
#Takes in a string or strings
def neg(numbers):
    matches = re.findall('-\d*', numbers)
    errorString = "Negatives not allowed: "
    for negative in matches:
        errorString += negative +','
    raise ValueError(errorString)


def add(numbers):
    result = 0
    delim = ','
    if numbers[:2] == '//':
        if re.match('//(\[.*?\])', numbers) is not None:
            delim = re.findall(r'\[([^]]*)\]', numbers.partition('\n')[0])[0]
        else:
            delim = numbers[2]
        if delim[0] in string.punctuation:
            t = ""
            for d in delim:
                t += '\\'+d
            delim = t

    endl = re.compile('{0}|\n'.format(delim))
    for number in re.split(endl,numbers):
        if '-' in number:
            neg(numbers)
        if number.isdigit() and int(number) < 1001:
            result += int(number)
    return result

