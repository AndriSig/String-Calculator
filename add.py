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

def findDelim(numbers):
    delim = ''
    if re.match('//(\[.*?\])', numbers) is not None:
        delim = re.findall(r'\[([^]]*)\]', numbers.partition('\n')[0])
    else:
        if numbers[2] in string.punctuation:
                delim = '\{0}'.format(numbers[2])
        else:
            delim = numbers[2]
    t = "["
    if not isinstance(delim, str):
        for d in delim:
            t += '('
            for i in d:
                 if i in string.punctuation:
                    t += '\{0}'.format(i)
                 else:
                     t += i
            t += ')'
        delim = t + ']'
    return delim

def add(numbers):
    endl = ',|\n'
    if numbers[:2] == '//':
        endl = re.compile(findDelim(numbers))
        numbers = numbers.partition('\n')[2]
    result = 0
    for number in re.split(endl,numbers):
        if '-' in number:
            neg(numbers)
        if number.isdigit():
            if int(number) < 1001:
                result += int(number)
    return result

