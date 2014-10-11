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

sum = ""
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
for i in range(1, 101):
    sum += '{0},'.format(i)
if add(sum) == 5050:
    res(1, '1,2,...,100', 1)
else:
    res(1, '1,2,...,100', 0)
sum = ""
for i in range(1, 100000):
    sum += '{0},'.format(i)
if add(sum) == 5000050000:
    res(1, '1,2,...,10^5', 1)
else:
    res(1, '1,2,...,10^5', 0)
