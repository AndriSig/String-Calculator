#!/usr/bin/python
import sys
import unittest
import string
import stringCalculator
import re

class BasicAdditionTest(unittest.TestCase):
    #Test 1
    #An empty input should return 0
    def testEmptyStr(self):
        self.assertEqual(stringCalculator.add(""), 0)
    #Test 2
    #A single number input should return that number
    def testOneStr(self):
        self.assertEqual(stringCalculator.add("1"), 1)
    #Test 3
    #A string with two numbers using , as delimiter should return the sum of those numbers
    def testOneTwoStr(self):
        self.assertEqual(stringCalculator.add("1,2"),3)
    #Test 4
    #New line should be interchangable with comma as a delimiter
    def testOneEndl(self):
        self.assertEqual(stringCalculator.add("1\n2,3"), 6)
    #Test 5
    #New line should be able to entirely replace comma as a delimiter
    def testTwoEndl(self):
        self.assertEqual(stringCalculator.add("1\n2\n3"), 6)
    #Test 6
    #Stress Testing newline as delimiter
    def testStaggeredEndl(self):
        sum = ""
        delim = [',','\n']
        for i in range(1, 100001):
            sum += '{0}{1}'.format(i,delim[i%2])
        self.assertEqual(stringCalculator.add(sum),5000050000)
    #Test 7
    #Make sure add is using the delimiter returned by findDelim properly
    def testAddFindDelimUse(self):
        for punct in string.punctuation:
            self.assertEqual(stringCalculator.add('//{0}\n1{0}2'.format(punct)),3)
        
class AdditionRangeTest(unittest.TestCase):
    #Test 1
    #Sum series from 1 to 100 results in 5050
    def testHundred(self):
        sum = ""
        for i in range(1,101):
            sum += '{0},'.format(i)
        self.assertEqual(stringCalculator.add(sum),5050)
    #Test 2
    #Sum series from 1 to 100000 results in 5000050000
    def testHundredK(self):
        sum = ""
        for i in range (1,100001):
            sum += '{0},'.format(i)
        self.assertEqual(stringCalculator.add(sum), 5000050000)
class findDelimTest(unittest.TestCase):
    #Test 1
    #findDelim should find the delimiter and return it, in this case ;
    def testNewDelim(self):
        self.assertEqual(stringCalculator.findDelim("//;\n1;2;3"), re.escape(';'))
    #Test 2
    #findDelim should be able to return any ascii letter as a delim
    def testAsciiDelim(self):
        for letter in string.ascii_letters:
            self.assertEqual(stringCalculator.findDelim('//{0}\n1{0}2'.format(letter)),letter)
    def testPunctDelim(self):
        for punct in string.punctuation:
            self.assertEqual(stringCalculator.findDelim('//{0}\n1{0}2'.format(punct)),re.escape(punct))
    def testWhiteSpaceDelim(self):
        for white in string.whitespace:
            self.assertEqual(stringCalculator.findDelim('//{0}\n1{0}2'.format(white)),re.escape(white))
def main():
    unittest.main()

if __name__ == '__main__':
    main()
