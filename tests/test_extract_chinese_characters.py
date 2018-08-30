#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 14:00
# @Author  : kaiwen Xue
# @File    : test_extract_chinese_characters.py
# @Software: PyCharm
import unittest
from kaiwen import extract_chinese_characters


class TestExtractChineseNumbers(unittest.TestCase):

    def test_extract_chinese_numbers(self):
        self.assertEqual(extract_chinese_characters('tes测t ex试tract chin提ese取 中chara文cters'), '测试提取中文')
        self.assertEqual(extract_chinese_characters('tes测t ex试tract chin提ese取 中chara文cters', type=list),
                         ['测', '试', '提', '取', '中', '文'])
        self.assertEqual(extract_chinese_characters('tes测t ex试tract chin提ese取 中chara文cters', ext=reversed),
                         'test extract chinese characters')
        self.assertEqual(extract_chinese_characters('tes测t ex试tract chin提ese取 中chara文cters', type=list, ext=reversed),
                         ['tes', 't ex', 'tract chin', 'ese', 'chara', 'cters'])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)