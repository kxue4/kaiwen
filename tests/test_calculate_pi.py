#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 16:20
# @Author  : kaiwen Xue
# @File    : test_calculate_pi.py
# @Software: PyCharm
import unittest
from kaiwen.calculate_pi import calculate_pi


class TestCalculatePi(unittest.TestCase):

    def test_calculate_pi(self):
        self.assertEqual(calculate_pi(100), '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
