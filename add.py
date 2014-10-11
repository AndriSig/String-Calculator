#!/usr/bin/python
import sys
import re
import unittest
#Takes in a string or strings
def add(numbers):
    result = 0
    endl = re.compile(',|\n')
    for number in re.split(endl,numbers):
        if number.isdigit():
            result += int(number)
    return result

def res(testNr, inp, res):
    pf = [ 'Failed','Passed']
    print('add({0}) Unit test Nr {1}: {2}'.format(inp, testNr, pf[res])) 


