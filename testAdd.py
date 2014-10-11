#!/usr/bin/python
import sys
import unittest
import add

 
#Tests the basic additive function of the method
class BasicAdditionTest(unittest.TestCase):
    #Test 1
    def testEmptyStr(self):
        self.assertTrue(add.add("") == 0)
    #Test 2
    def testOneStr(self):
        self.assertTrue(add.add("1") == 1)
    #Test 3
    def testOneTwoStr(self):
        self.assertTrue(add.add("1,2") == 3)
    #Test 4

#Tests if the function can handle arbitrary ranges
class AdditionRangeTest(unittest.TestCase):
    #Test 5
    def testHundred(self):
        sum = ""
        for i in range(1, 101):
            sum += '{0},'.format(i)
        self.assertTrue(add.add(sum) == 5050)
    #Test 6
    def testHundredK(self):
        sum = ""
        for i in range(1, 100001):
            sum += '{0},'.format(i)
        self.assertTrue(add.add(sum) == 5000050000)

class AdditionDelimTest(unittest.TestCase):
    def testOneEndl(self):
        self.assertTrue(add.add("1\n2,3") == 6)
    def testTwoEndl(self):
        self.assertTrue(add.add("1\n2\n3") == 6)
    def testStaggeredEndl(self):
        sum = ""
        delim = [',','\n']
        for i in range(1, 100001):
            sum += '{0}{1}'.format(i,delim[i%2])
        self.assertTrue(add.add(sum) == 5000050000)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
