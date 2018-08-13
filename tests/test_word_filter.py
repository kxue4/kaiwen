#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/11/18 20:33
# @Author  : Kaiwen Xue
# @File    : test_word_filter.py
# @Software: PyCharm
import unittest
from unittest import mock
from Kaiwen.word_filter import *


class TestWordFilter(unittest.TestCase):
    @mock.patch('word_filter.get_user_input')
    def test_word_filter(self, mock_get_user_input):
        mock_get_user_input.return_value = 'Holy shit! What the fuck?'
        self.assertEqual(word_replace(), 'Holy ****! What the ****?')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)