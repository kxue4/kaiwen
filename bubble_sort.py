#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/1/18 21:53
# @Author  : Kaiwen Xue
# @File    : bubble_sort.py
# @Software: PyCharm


def bubble_sort(list):
    n = len(list)
    count = 0

    for j in range(n - 1):

        for i in range(0, n - 1 - j):

            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                count += 1

    return list, count
