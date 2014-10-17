#!/usr/bin/python
import sys
import re
import unittest
import string

def add(numbers):
    result = 0
    for num in re.split(r',', numbers):
        if num.isdigit():
            result += int(num)
    return result
  