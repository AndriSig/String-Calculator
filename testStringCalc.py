#!/usr/bin/python
import sys
import unittest
import string
import stringCalculator

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


def main():
    unittest.main()

if __name__ == '__main__':
    main()
