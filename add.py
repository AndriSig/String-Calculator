#!/usr/bin/python
import sys
#Takes in a string or strings
def add(numbers):
    result = 0
    for number in numbers.rsplit(','):
        if number.isdigit():
            result += int(number)
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
    res(2, '1', 1)
else:
    res(2, '1', 0)
#Test 3
if add("1,2") == 3:
    res(3, '1,2', 1)
else:
    res(3, '1,2', 0)
#Test 4
for i in range(1, 101):
    sum += '{0},'.format(i)
if add(sum) == 5050:
    res(4, '1,2,...,100', 1)
else:
    res(4, '1,2,...,100', 0)
sum = ""
#Test 5
for i in range(1, 100001):
    sum += '{0},'.format(i)
if add(sum) == 5000050000:
    res(5, '1,2,...,10^5', 1)
else:
    res(5, '1,2,...,10^5', 0)
#Test 6
if add("1\n2,3") == 6:
    res(6, "1\\n2,3", 1)
else:
    res(6, "1\\n2,3", 0)
#Test 7
if add("1\n2\n3") == 6:
    res(6, "1\\n2\\n3", 1)
else:
    res(6, "1\\n2\\n3", 0)

