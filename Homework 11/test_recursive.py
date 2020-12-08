"""
Homework #11
CSCI-UA. 0003-001 Fall 2020
Edmund Cheng
ec3219
2020-12-06
"""


import unittest
from recursive import count_nested_tuple

#  write your test class here!
# I made two test cases; 1 for tuple, 1 for nested tuple


class TestRecursive(unittest.TestCase):
    def test_tuple(self):
        count = 7
        tup = (1, 2, 3, 4, 5, 6, 7)
        t = count_nested_tuple(tup)
        self.assertEqual(count, t)

    def test_nested_tuple(self):
        count = 10
        tup = (1, (2, 3), 4, (5, 6, 7), (8, 9), 10)
        t = count_nested_tuple(tup)
        self.assertEqual(count, t)


if __name__ == '__main__':
    unittest.main()