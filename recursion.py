#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 17:52
# @Author  : Kaiwen Xue
# @File    : recursion.py
# @Software: PyCharm


def sum_it(foo):

    if len(foo) == 1:
        return foo[0]
    else:
        return foo.pop() + sum_it(foo)
