#!/usr/bin/env python
# -*- coding:utf8 -*-

#套一个大循环，循环下一页
import requests
import re
# 大学生群体
# 数据的爬取采集
# 数据的存储
# 数据的处理/过滤/筛选
# 数据的分析与展示


# 1、要知道去哪里爬取想要的数据
# 2、要分析这个地址的结构或解析

# /d/file/20171202/3226be099ad8d610e92bbab5218047d1.jpg"
#
# 加入一个循环 按照某个标准循环
# 写成一个jpg的文件
import requests
import re
url = 'http://www.xiaohuar.com/list-1-%s.html'
for i in range(4):
    temp = url % i
    print(temp)
#h获取网页的源码
    response =requests.get(temp)
#从源码里面，获取我们想要的图片的url（图片地址）
    html = response.text
#/d/file/20171202/3226be099ad8d610e92bbab5218047d1.jpg
# /d/file/20170919/2f728d0f110a21fea95ce13e0b010d06.jpg
# /d/file/20170917/715515e7fe1f1cb9fd388bbbb00467c2.jpg
# /d/file/20170916/7f78145b1ca162eb814fbc03ad24fbc1.jpg
#写正则表达式
    img_urls=re.findall(r"/d/file/\d+/\w+\.jpg",html)
#循环获取图片的url
    for img_url in img_urls:
        img_response=requests.get("http://www.xiaohuar.com%s" %img_url)
        print(img_url)
        img_data=img_response.content #二进制信息


        xiaohua=img_url.split('/')[-1]#差分并且切割，娶她最后一个值
        with open(xiaohua,'wb')as f: # 写入文件的一个格式
            f.write(img_data)