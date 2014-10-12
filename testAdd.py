#!/usr/bin/python
import sys
import unittest
import add
import string

 
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
    def testThousandOneStr(self):
        self.assertTrue(add.add('1,2,3,1001,2001') == 6)

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
        self.assertTrue(add.add(sum) == 500500) #digits larger than 1000 should be ignored

class AdditionDelimTest(unittest.TestCase):
    #Test 7
    def testOneEndl(self):
        self.assertTrue(add.add("1\n2,3") == 6)
    #Test 8
    def testTwoEndl(self):
        self.assertTrue(add.add("1\n2\n3") == 6)
    #Test 9
    def testStaggeredEndl(self):
        sum = ""
        delim = [',','\n']
        for i in range(1, 100001):
            sum += '{0}{1}'.format(i,delim[i%2])
        self.assertTrue(add.add(sum) == 500500)
    #Test 10
    def testNewDelim(self):
        self.assertTrue(add.add("//;\n1;2"))
    #Test 11
    def testAsciiDelim(self):
        for letter in string.ascii_letters:
            self.assertTrue(add.add('//{0}\n1{0}2'.format(letter)) == 3)
    def testPunctDelim(self):
        for punct in string.punctuation:
            self.assertTrue(add.add('//{0}\n1{0}2'.format(punct)) == 3)
    def testWhiteSpaceDelim(self):
        for white in string.whitespace:
            self.assertTrue(add.add('//{0}\n1{0}2'.format(white)) == 3)
    def testLongDelim(self):
        self.assertTrue(add.add('//[***]\n1***2***3') == 6)
    def testAsciiLongDelim(self):
        for letter in string.ascii_letters:
            self.assertTrue(add.add('//[{0}{0}{0}]\n1{0}2'.format(letter)) == 3)
    def testPunctLongDelim(self):
        for punct in string.punctuation:
            self.assertTrue(add.add('//[{0}{0}{0}]\n1{0}2'.format(punct)) == 3)
    def testWhiteLongSpaceDelim(self):
        for white in string.whitespace:
            self.assertTrue(add.add('//[{0}{0}{0}]\n1{0}2'.format(white)) == 3)
    def testAsciiLongerDelim(self):
        for letter in string.ascii_letters:
            delim = ""
            for i in range(0, 30):
                delim += letter
            self.assertTrue(add.add('//[{0}]\n1{0}2'.format(letter)) == 3)


class AdditionExceptionTest(unittest.TestCase):
    def testSingleNegativeInput(self):
        with self.assertRaisesRegexp(ValueError, 'Negatives not allowed: -3'):
            add.add( "1,2,-3")
    def testMultipleNegativeInputs(self):
        with self.assertRaisesRegexp(ValueError, 'Negatives not allowed: -2,-5,-8'):
            add.add( "1,-2,5,-5,6,7,-8")
def main():
    unittest.main()

if __name__ == '__main__':
    main()
