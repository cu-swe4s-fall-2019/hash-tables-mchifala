import unittest
import random
import os
import numpy as np
import sys
from hash_functions import h_ascii
from hash_functions import h_rolling
import string


class TestHash(unittest.TestCase):

    def test_hash_empty(self):
        self.n = 10
        self.assertEqual(0, h_ascii("", self.n))
         
    def test_hash(self):
        self.n = 10
        self.asciiDict = {chr(i): i for i in range(129)} 
        self.random_string = ''.join(random.choices(string.ascii_letters, k=10))
        self.sum = 0
        for char in self.random_string:
            self.sum += self.asciiDict[char]
        self.hash_value = self.sum % self.n      
        self.assertEqual(self.hash_value, h_ascii(self.random_string, self.n))
        
    def test_hash_no_table(self):
        self.n = 0
        self.random_string = ''.join(random.choices(string.ascii_letters, k=10))    
        self.assertRaises(ZeroDivisionError and SystemExit, 
                          h_ascii, self.random_string, self.n)
        
    def test_rolling_hash_empty(self):
        self.n = 10
        self.assertEqual(0, h_rolling("", self.n))
        
    def test_rolling_hash(self):
        self.n = 10
        self.m = 2^64
        self.p = 53
        self.asciiDict = {chr(i): i for i in range(129)} 
        self.random_string = ''.join(random.choices(string.ascii_letters, k=10))
        self.sum = 0
        for c, char in enumerate(self.random_string):
            self.sum += self.asciiDict[char] * self.p ** c
        self.hash_value = (self.sum % self.m) % self.n      
        self.assertEqual(self.hash_value, h_rolling(self.random_string, self.n))
        
    def test_rolling_hash_no_table(self):
        self.n = 0
        self.random_string = ''.join(random.choices(string.ascii_letters, k=10))    
        self.assertRaises(ZeroDivisionError and SystemExit, 
                          h_rolling, self.random_string, self.n)
    
    
if __name__ == '__main__':
    unittest.main()
