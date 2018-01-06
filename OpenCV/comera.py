#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-01 16:23:32
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : https://github.com/Yeharold

import cv2 


comera = cv2.VideoCapture(0)


while True:

	res,frame = comera.read()
	cv2.imshow('harold', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.imwrite("harold.jpeg", frame)
		break
	
comera.release()
cv2.destroyAllWindows()
