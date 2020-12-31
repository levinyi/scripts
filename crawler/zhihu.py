#!/usr/bin/python3 
# coding:utf-8
import re
from selenium import webdriver
import time
import urllib.request

#driver = webdriver.Chrome(r"C:\Users\dushiyi\AppData\Local\Google\Chrome\Application\chromedriver.exe") # my windows 
driver = webdriver.Chrome("/Users/shiyidu/Downloads/chromedriver") # my mac 
# print("haha")
# '''
# driver.maximize_window() # 最大化浏览器窗口
driver.get("https://zhuanlan.zhihu.com/p/28017094")
# print("haha")

#这段代码有待进一步研究
i = 0
while i<10:
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
	time.sleep(2)
	try:
		driver.find_element_by_css_selector('button.QuestionMainAction').click() # 通过类class获取 http://www.cnblogs.com/paisen/p/3310395.html
		print("page"+ str(i))
	except :
		break

result_raw = driver.page_source # 网页源码
# print(result_raw)
content_list = re.findall("img src=\"(.+?)\" ",str(result_raw)) # 从网页源码中匹配jpg连接
# print(content_list) 
# n = 0
# while n <= len(content_list):
for each in content_list:
	i = time.time()
	local = (r"%s.jpg" %(i))
	urllib.request.urlretrieve(each,local) #打开url后,我们可以将内容写入一个本地文件来达到保存网页的目的,但是这里有一个更方便的方法,那就是调用urlretrieve()
	# print("number:"+str(i))
	# n += 1
print("download %s files"%len(content_list))
# '''
