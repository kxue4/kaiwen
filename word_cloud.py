#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 14:35
# @Author  : Kaiwen Xue
# @File    : word_cloud.py
# @Software: PyCharm
from wordcloud import WordCloud
import codecs
import jieba
from imageio import imread
import os
from os import path
import matplotlib.pyplot as plt


def draw_wordcloud():
    comment_text = open('source/word_cloud_text.txt', 'r').read()
    cut_text = " ".join(jieba.cut(comment_text))
    color_mask = imread("source/person.jpg")
    cloud = WordCloud(
        font_path="source/PingFang Regular.ttf",
        background_color='white',
        mask=color_mask,
        max_words=1000,
        max_font_size=150
    )
    word_cloud = cloud.generate(cut_text)
    word_cloud.to_file("source/wc_output.jpg")

    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    draw_wordcloud()
