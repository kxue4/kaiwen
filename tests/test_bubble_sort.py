#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/4/18 19:45
# @Author  : kaiwen Xue
# @File    : test_bubble_sort.py
# @Software: PyCharm
import unittest
from kaiwen.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([3, 2, 12, 7, 6, 9]), ([2, 3, 6, 7, 9, 12], 5))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)