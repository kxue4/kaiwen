#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/11/18 19:45
# @Author  : Kaiwen Xue
# @File    : word_filter.py
# @Software: PyCharm


def get_user_input():
    user_input = input('Please input something: ')
    return user_input


def word_replace():
    file = open('source/SensitiveWords.txt')
    words = file.readlines()
    user_input = get_user_input()
    filter_list = [word.strip() for word in words]

    for i in filter_list:
        number_of_star = len(i)
        user_input = user_input.replace(i, '*' * number_of_star)

    return user_input

