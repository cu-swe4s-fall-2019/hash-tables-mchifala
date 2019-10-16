import unittest
import random
import os
import numpy as np
import sys
from hash_functions import h_ascii
from hash_functions import h_rolling
from hash_functions import h_mult
from hash_tables import LinearProbe
from hash_tables import ChainedHash
from hash_scatter import scatter_plot
import string
from math import sqrt
from math import floor


class TestHash(unittest.TestCase):

    def make_rand_ascii_hash(self, n):
        """
        This helper function creates a random string of length 10 and
        calculates its hash value using the h_ascii strategy.

        """
        self.asciiDict = {chr(i): i for i in range(129)}
        self.rand_string = ''.join(random.choices(string.ascii_letters, k=10))
        self.sum = 0
        for char in self.rand_string:
            self.sum += self.asciiDict[char]
        return self.rand_string, self.sum % n

    def make_rand_mult_hash(self, n):
        """
        This helper function creates a random string of length 1- and
        calculates its hash value using the multiplicative hash strategy.

        """
        self.A = (sqrt(5)-1)/2
        self.asciiDict = {chr(i): i for i in range(129)}
        self.rand_string = ''.join(random.choices(string.ascii_letters, k=10))
        self.sum = 0
        for char in self.rand_string:
            self.sum += self.asciiDict[char]

        return self.rand_string, floor(self.n*((self.sum*self.A) % 1))

    def make_rand_rolling_hash(self, n):
        """
        This helper function creates a random string of length 10 and
        calculates its hash value using the poly. rolling hash strategy.

        """
        self.m = 2**64
        self.p = 53
        self.asciiDict = {chr(i): i for i in range(129)}
        self.rand_string = ''.join(random.choices(string.ascii_letters, k=10))
        self.sum = 0
        for c, char in enumerate(self.rand_string):
            self.sum += self.asciiDict[char] * self.p ** c
        return self.rand_string, (self.sum % self.m) % self.n

    def test_ascii_hash_empty(self):
        """
        This test checks h_ascii function on an empty string

        """
        self.n = 10
        self.assertEqual(0, h_ascii("", self.n))

    def test_ascii_hash(self):
        """
        This test checks h_ascii function on a random string of length 10

        """
        self.n = 10
        self.rand_string, self.hash_value = self.make_rand_ascii_hash(self.n)

        self.assertEqual(self.hash_value, h_ascii(self.rand_string, self.n))

    def test_asci_hash_no_table(self):
        """
        This test checks h_ascii function on a random string of length 10
        when n = 0

        """

        self.n = 0
        self.rand_string = ''.join(random.choices(string.ascii_letters, k=10))
        self.assertRaises(ZeroDivisionError and SystemExit,
                          h_ascii, self.rand_string, self.n)

    def test_mult_hash_empty(self):
        """
        This test checks h_ascii function on an empty string

        """
        self.n = 10
        self.assertEqual(0, h_mult("", self.n))

    def test_mult_hash(self):
        """
        This test checks h_ascii function on a random string of length 10

        """
        self.n = 10
        self.rand_string, self.hash_value = self.make_rand_mult_hash(self.n)
        self.assertEqual(self.hash_value, h_mult(self.rand_string, self.n))

    def test_rolling_hash_empty(self):
        """
        This test checks  h_rolling function on an empty string

        """
        self.n = 10
        self.assertEqual(0, h_rolling("", self.n))

    def test_rolling_hash(self):
        """
        This test checks h_rolling function on a random string of length 10

        """
        self.n = 10
        self.rand_string, self.hash_value = self.make_rand_rolling_hash(self.n)
        self.assertEqual(self.hash_value, h_rolling(self.rand_string, self.n))

    def test_rolling_hash_no_table(self):
        """
        This test checks h_rolling function on a random string of length 10
        when n = 0

        """
        self.n = 0
        self.rand_string = ''.join(random.choices(string.ascii_letters, k=10))

        self.assertRaises(ZeroDivisionError and SystemExit,
                          h_rolling, self.rand_string, self.n)

    def test_hash_lp_empty(self):
        """
        This test checks LinearProbe add function on a empty table

        """
        self.n = 10
        self.value = "Hello"
        self.inst_table = LinearProbe(self.n, h_ascii)
        self.key, self.hash_value = self.make_rand_ascii_hash(self.n)
        self.assertTrue(self.inst_table.add(self.key, self.value))

    def test_hash_lp_full(self):
        """
        This test checks LinearProbe add function on a full table

        """
        self.n = 10
        self.value = "Hello"
        self.key, self.hash_value = self.make_rand_ascii_hash(self.n)
        self.inst_table = LinearProbe(self.n, h_ascii)
        self.inst_table.table = ["Full" for i in range(self.n)]
        self.assertFalse(self.inst_table.add(self.key, self.value))

    def test_hash_lp_search_empty(self):
        """
        This test checks LinearProbe search function on empty table
        where the key does not exist

        """
        self.n = 10
        self.key, self.hash_value = self.make_rand_ascii_hash(self.n)
        self.inst_table = LinearProbe(self.n, h_ascii)
        self.assertEqual(None, self.inst_table.search(self.key))

    def test_hash_lp_search_full(self):
        """
        This test checks LinearProbe search function on a full table
        where the key exists

        """
        self.n = 10
        self.inst_table = LinearProbe(self.n, h_ascii)
        self.inst_table.table = [(chr(x), x) for x in range(self.n)]
        self.assertTrue(1, self.inst_table.search(chr(1)))

    def test_hash_lp_search_partial(self):
        """
        This test checks LinearProbe search function on a partially full table
        where the key does not exist

        """
        self.n = 10
        self.inst_table = LinearProbe(self.n, h_ascii)
        self.inst_table.table = [(chr(x), x) for x in range(self.n)]
        self.inst_table.table[5] = (chr(15), 15)
        self.inst_table.table[6] = None
        self.assertEqual(None, self.inst_table.search(chr(5)))

    def test_hash_chain_empty(self):
        """
        This test checks ChainedHash add function on a empty table

        """
        self.n = 10
        self.value = "Hello"
        self.inst_table = ChainedHash(self.n, h_ascii)
        self.key, self.hash_value = self.make_rand_ascii_hash(self.n)
        self.assertTrue(self.inst_table.add(self.key, self.value))

    def test_hash_chain_full(self):
        """
        This test checks ChainedHash add function on a table with
        one entry in each linked list

        """
        self.n = 10
        self.value = "Hello"
        self.inst_table = ChainedHash(self.n, h_ascii)
        self.inst_table.table = [[(chr(x), x)] for x in range(self.n)]
        self.key, self.hash_value = self.make_rand_ascii_hash(self.n)
        self.assertTrue(self.inst_table.add(self.key, self.value))

    def test_hash_chain_search_full(self):
        """
        This test checks LinearProbe search function on a full table
        with multiple elementes in each linked list
        """
        self.n = 10
        self.inst_table = ChainedHash(self.n, h_ascii)
        self.inst_table.table = [[(chr(x), x),
                                  (chr(x+self.n),
                                   x+self.n)] for x in range(self.n)]

        self.assertEqual(5, self.inst_table.search(chr(5)))

    def test_hash_chain_search_empty(self):
        """
        This test checks LinearProbe search function on an empty table
        where the key exists

        """
        self.n = 10
        self.inst_table = ChainedHash(self.n, h_ascii)
        self.assertEqual(None, self.inst_table.search(chr(5)))

    def test_boxplot_exist(self):
        """
        This test checks to see if file exists after scatterplot is created

        """
        self.x_data = [x for x in range(10)]
        self.y_data = self.x_data
        self.x_label = "X"
        self.y_label = "Y"
        self.title = "Title"
        self.outfile = "test.png"
        scatter_plot(self.x_data, self.y_data, self.x_label, self.y_label,
                     self.title, self.outfile)
        self.assertEqual(True, os.path.exists(self.outfile))


if __name__ == '__main__':
    unittest.main()
