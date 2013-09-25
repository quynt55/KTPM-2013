'''
Created on Sep 23, 2013

@author: nguyenquy
'''
import unittest
from __init__ import detect_triangle
import math

class Test(unittest.TestCase):

    def testName1(self):
        self.assertEqual(detect_triangle(-1,1,3), "Nhap sai")
    def testName2(self):
        self.assertEqual(detect_triangle(1,-1,3), "Nhap sai")
    def testName3(self):
        self.assertEqual(detect_triangle(1,1,-3), "Nhap sai")
    def testName4(self):
        self.assertEqual(detect_triangle("a",5,6), "Nhap sai")
    def testName5(self):
        self.assertEqual(detect_triangle(5,"a",6), "Nhap sai")
    def testName6(self):
        self.assertEqual(detect_triangle(5,6,"a"), "Nhap sai")
    def testName7(self):
        self.assertEqual(detect_triangle(1,1,3), "Khong phai la ba canh tam giac!")
    def testName8(self):
        self.assertEqual(detect_triangle(1,3,1), "Khong phai la ba canh tam giac!")
    def testName9(self):
        self.assertEqual(detect_triangle(3,1,1), "Khong phai la ba canh tam giac!")
    def testName10(self):
        self.assertEqual(detect_triangle(3,3,3), "Tam giac deu")
    def testName11(self):
        self.assertEqual(detect_triangle(3,2,3), "Tam giac can")
    def testName12(self):
        self.assertEqual(detect_triangle(3,3,2), "Tam giac can")
    def testName13(self):
        self.assertEqual(detect_triangle(2,3,3), "Tam giac can")
    def testName14(self):
        self.assertEqual(detect_triangle(3,4,5), "Tam giac vuong")
    def testName15(self):
        self.assertEqual(detect_triangle(3,5,4), "Tam giac vuong")
    def testName16(self):
        self.assertEqual(detect_triangle(5,4,3), "Tam giac vuong")
    def testName17(self):
        self.assertEqual(detect_triangle(1,1,math.sqrt(2)), "Tam giac vuong can")
    def testName18(self):
        self.assertEqual(detect_triangle(1,math.sqrt(2),1), "Tam giac vuong can")
    def testName19(self):
        self.assertEqual(detect_triangle(math.sqrt(2),1,1), "Tam giac vuong can")
    def testName20(self):
        self.assertEqual(detect_triangle(3,5,6), "Tam giac thuong")
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()