#!/usr/bin/python
import sys

def add(numbers):
    result = 0
    numbers.rsplit(',')
    for i in range(0,len(numbers)):
        if i > 2:
            break
        if numbers[i].isdigit():
            result += int(numbers[i])
    return result

def res(testNr, inp, res):
    pf = [ 'Failed','Passed']
    print('add({0}) Unit test Nr {1}: {2}'.format(inp, testNr, pf[res])) 

#Test 1
if add("") == 0:
    res(1, '""', 1)
else:
    res(1, '""', 0)
#Test 2
if add("1") == 1:
    res(1, '1', 1)
else:
    res(1, '1', 0)
#Test 3
if add("1,2") == 3:
    res(1, '1,2', 1)
else:
    res(1, '1,2', 0)
#Test 4
if add("1,2,3") == 3:
    res(1, '1,2,3', 1)
else:
    res(1, '1,2,3', 0)
