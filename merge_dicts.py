#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 11:27
# @Author  : Kaiwen Xue
# @File    : merge_dicts.py
# @Software: PyCharm


def merge_dicts(*args):
    n = len(args)
    i = 1
    while i < n:

        for key, value in args[i].items():

            if key in args[0].keys():
                args[0][key] += value
            else:
                args[0][key] = value

        i += 1

    return args[0]
