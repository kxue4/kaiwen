#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 15:56
# @Author  : Kaiwen Xue
# @File    : test_recursion.py
# @Software: PyCharm
import unittest
from recursion import sum_it


class TestSumIt(unittest.TestCase):

    def test_sum_it(self):
        self.assertEqual(sum_it([1, 2, 3, 100]), 106)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)