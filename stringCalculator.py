#!/usr/bin/python
import sys
import re
import unittest
import string

def add(numbers):
    result = 0
    delim = ',|\n'
    if numbers[:2] is '\\':
        delim = findDelim(numbers)
    for num in re.split(delim, numbers):
        if num.isdigit():
            result += int(num)
    return result
  
def findDelim(input):
    return input[2]
