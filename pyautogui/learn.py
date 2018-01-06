#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-29 18:37:42
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : https://github.com/Yeharold

import pyautogui as m
import face_recognition as face
import cv2
import time as t 

comera = cv2.VideoCapture(0)


harold = face.load_image_file("harold.jpg")
harold_en = face.face_encodings(harold)[0]



while True:
    ret, frame = comera.read()
    cv2.imshow('harold', frame)

    t.sleep(3q)
    face_locations = face.face_locations(frame)
    if len(face_locations)>0:

        face_ens = face.face_encodings(frame, face_locations)

        for face_en in face_ens:
            match = face.compare_faces([harold_en], face_en)


            if match[0]:
            	print("harold")
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


comera.release()
cv2.destroyAllWindows()

