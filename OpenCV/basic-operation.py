#!/usr/bin/python2
# -*- coding: utf-8 -*-
# @Date    : 2017-12-24 20:34:24
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : https://github.com/Yeharold

import cv2
import numpy as np 

img = cv2.imread('lena.jpg')

cv2.imshow('lena',img)
cv2.waitKey(0)