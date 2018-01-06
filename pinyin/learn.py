#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-02 19:34:51
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : https://github.com/Yeharold

from pypinyin import pinyin as chinese


text = "你好中国"
res = chinese(text)

print(res)
