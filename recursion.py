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


def quick_sort(foo):

    if len(foo) < 2:
        return foo
    else:
        pivot = foo[0]
        smaller = [i for i in foo[1:] if i < pivot]
        larger = [i for i in foo[1:] if i > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(larger)