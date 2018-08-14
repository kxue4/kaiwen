#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/11/18 20:33
# @Author  : Kaiwen Xue
# @File    : test_word_filter.py
# @Software: PyCharm
import unittest
from Kaiwen.word_filter import word_filter


class TestWordFilter(unittest.TestCase):
    def test_word_filter(self):
        self.assertEqual(word_filter('Holy shit! What the fuck?'), 'Holy ****! What the ****?')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)