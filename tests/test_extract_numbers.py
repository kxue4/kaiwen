#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 10:37
# @Author  : kaiwen Xue
# @File    : test_extract_numbers.py
# @Software: PyCharm
import unittest
from ggre import extract_numbers


class TestExtractNumbers(unittest.TestCase):

    def test_extract_numbers(self):
        self.assertEqual(extract_numbers('tes4t ext5ract n2umbers'), '452')
        self.assertEqual(extract_numbers('tes4t ext5ract n2umbers', type=list), ['4', '5', '2'])
        self.assertEqual(extract_numbers('tes4t ext5ract n2umbers', ext=reversed), 'test extract numbers')
        self.assertEqual(extract_numbers('tes4t ext5ract n2umbers', type=list, ext=reversed), ['tes', 't ext', 'ract n',
                                                                                             'umbers'])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)