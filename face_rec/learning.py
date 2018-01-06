#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-01 13:24:43
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : https://github.com/Yeharold

import face_recognition as face 
from PIL import Image,ImageDraw

img = face.load_image_file("test.jpg")
location = face.face_locations(img)

img = Image.fromarray(img)

draw = ImageDraw.Draw(img)


for (top, right, bottom, left) in location:
	box = (left,top,right,bottom)

	draw.rectangle(box)

img.show()

