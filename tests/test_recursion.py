#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 15:56
# @Author  : Kaiwen Xue
# @File    : test_recursion.py
# @Software: PyCharm
import unittest
from Kaiwen.recursion import sum_it, quick_sort


class TestRecursion(unittest.TestCase):

    def test_sum_it(self):
        self.assertEqual(sum_it([1, 2, 3, 100]), 106)

    def test_quick_sort(self):
        self.assertEqual(quick_sort([3, 2, 8, 7, 6, 1, 100]), [1, 2, 3, 6, 7, 8, 100])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)