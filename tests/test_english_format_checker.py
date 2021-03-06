#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 16:48
# @Author  : kaiwen Xue
# @File    : test_english_format_checker.py
# @Software: PyCharm
import unittest
from kaiwen.english_format_checker import english_format_checker


class TestEnglishFormatChecker(unittest.TestCase):

    def test_englisht_format_checker(self):
        self.assertEqual(english_format_checker
                         ('capitalize this,Lower this and add blank. This sentence is perfect.'),
                         'Capitalize this, lower this and add blank. This sentence is perfect.')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)