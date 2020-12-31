#!/usr/bin/python3
# 2017.11.04 11:06:29 CST
# 2017.11.04 22:59:25 CST
"""
[Python OpenCV 图像处理实现细胞计数](https://zhuanlan.zhihu.com/p/30723580)
"""

import cv2
import numpy as np

## 读取图像
img = cv2.imread("default.jpeg")

## 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## 高斯滤波
gauss  = cv2.GaussianBlur(gray, (5,5), 0)
# print(gauss)

## 二值化
_, threshed = cv2.threshold(gauss, 150, 255, cv2.THRESH_BINARY_INV )
# print(threshed)

## 获取结构基元，进行形态学滤波
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
morphed = cv2.morphologyEx(threshed, cv2.MORPH_OPEN, kernel, None, (-1,-1), 1)

## 获取边缘
_, cnts, _ = cv2.findContours(morphed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

## 绘制
canvas = img.copy()
cv2.drawContours(canvas,cnts, -1,  (0,200,200), 1)

## 筛选并绘制
xcnts = []
for cnt in cnts:
    area = cv2.contourArea(cnt)
    x,y,w,h = cv2.boundingRect(cnt)
    if area < 12 or area/(w*h) < 0.3:
        continue
    xcnts.append(cnt)
    print(cnt)
cv2.drawContours(canvas, xcnts, -1,  (100,20,200),1)

print("Cells nums: {}/{}".format(len(xcnts), len(cnts)))

## 显示结果
cv2.imshow("src", img)
cv2.imshow("dst", canvas)
cv2.waitKey()
cv2.destroyAllWindows()



