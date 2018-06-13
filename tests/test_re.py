#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 10:25
# @Author  : Kaiwen Xue
# @File    : test_re.py
# @Software: PyCharm
import unittest
from my_re import extract_chinese_character, extract_numbers


class TestMyRE(unittest.TestCase):

    def test_extract_chinese_character(self):
        self.assertEqual(extract_chinese_character('sjfw.20df测试通过sm2d-2了'), '测试通过了')

    def test_extract_numbers(self):
        self.assertEqual(extract_numbers('sdjflj201.,?sjf8'), '2018')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)