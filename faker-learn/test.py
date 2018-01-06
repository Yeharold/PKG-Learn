#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-27 10:18:58
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : https://github.com/Yeharold

from faker import Faker 


f = Faker()

for i in range(50):
	print(f.name())