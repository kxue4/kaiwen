#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/12/18 21:17
# @Author  : Kaiwen Xue
# @File    : 001.py
# @Software: PyCharm
"""
有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
"""


n = 0

for i in range(1, 5):

    for j in range(1,5):

        for k in range(1,5):

            if i != j and j !=k and i !=k:
                print(i * 100 + j * 10 + k)
                n += 1

print(n)
