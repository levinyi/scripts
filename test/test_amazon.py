from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import requests
from lxml import html

'''
# driver = webdriver.Chrome('/cygene/script/test/chromedriver')
driver = webdriver.PhantomJS('/cygene/software/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.delete_all_cookies()
driver.get('https://www.amazon.com/')

########################################################################################################
driver.find_element_by_id("twotabsearchtextbox").send_keys('B01M6YE2M8')
driver.find_element_by_class_name("nav-input").click() # yes
driver.find_element_by_xpath("//div[contains(@class,'a-column a-span12 a-text-center')]//img[contains(@class,'s-access-image cfMarker')]").click() # yes
print(driver.current_url)

page = requests.get(driver.current_url,headers = {'User-Agent':'Mozilla/5.0'})

soup =BeautifulSoup(page.text,"lxml")

# print (soup.find_all("span",{'data-hook':'review-body'}))
# # print soup.find_all("a",{"id":"customer-reviews-content"})
# print (soup.find_all(attrs={"data-hook":"reviewe-date"})) # failed
# print (soup.find_all("span",{'data-hook':'review-body'}))
# # print soup.find_all("span",{'data-hook':'review-author'})
# print (soup.find_all("span",{'data-hook':'review-date'}))
for each in soup.find_all("div",{'data-hook':'review-collapsed'}):
	print("***********",each)
# print soup.select("body a")
# for each in soup.find_all(attrs={"data-hook":"review-date"}):
# 	print each
# print tree.xpath("//*[@id='customer_review-[4]']/div[4]/span/div/div/text()") # yes
# print soup.find_all("div",)
# print "soup is finding date... "
# result1 = soup.find_all(attrs={"data-hook":"review-date"})
# print "test",test
'''
########################################################################################################
items = ['B01KIQH2VU','B01B5ITZ4M','B01N44MTLJ','B01N4DFVLL','B01KG84CLI','B07B2Q3X75','B06W56XFQ4','B01M6YE2M8','B0798DDVN7','B00DVKJXFE','B078JCRHH6','B01FASX1T8','B07984TQ3C','B075VRJJT7','B07FCXYGFQ','B01B5ITXMQ','B01N5F3KPY','B01BDQTLTU','B071WK2XQR','B01N3Y3848','B00FPHLWVO','B007JLKXFU','B072NZLT27','B075DDFJJ8','B07C9CWDH6','B01M24BEJJ','B01N8TOPG2','B07FM1NDDM','B01G1J9GR6','B075TZB1VY','B0725HTHM2','B01GPQJVES','B07CWKB2NK','B072NZLT27','B079N96SKD','B0759YD8QH','B011SPT9XY','B072VHDQ74','B07BK3JB61','B0785DLJ9Q','B01ASMPYS2','B078J63LCJ','B075M941F3','B078T37FG5','B01L8UIIZ4','B07BK398S6','B071RTNYD3','B01N4NQ83I','B073FX3MV1','B07DYCVDVY','B01N4NQ83I','B073FX3MV1','B00N46TNAU','B01ASMPXGK','B07CWKNS54','B075TZ5F5L','B00LJR51AW','B01HM56LZS','B07F1M7X7R','B076F26448','B00KH1W54Q','B06XZT86CL','B07CLJKFZK','B000KJZOWU','B00K6K4SOS','B07CXCZHDN','B078N5JNJV','B07DJ7TJB4','B01KIPV7JE','B007JYZW3U','B07CLJKFZK','B077XXL9QH','B07DR7R3LQ','B076RQR8CH','B07C1KXCLC','B004XIWN3M','B01H8B9O46','B00AIVN89G','B00FRS2C2E','B07B3NHGBN','B000T5PMZ4','B072VH9LZF','B075V2VB49','B0149KSJTK','B0099SCDLI','B007JYZW08','B07CZZG2Y6','B01HM804MQ','B078J8D61V','B019BJUF0U','B00CY8D57Q','B078N9KRGW','B00ODEPQBW','B07CG5PXL3','B071JNN9QN','B07CZ785XC','B0193XGZ7G','B07FBGW6C1','B0721FQWX7','B000UD3ZGI',]
'''
print("there are %s items."%len(items))
current_urls =[]
for each in items:
	driver.find_element_by_id("twotabsearchtextbox").send_keys(each)
	driver.find_element_by_class_name("nav-input").click() # yes
	# driver.find_element_by_id('result_0').click()
	driver.find_element_by_xpath("//div[contains(@class,'a-column a-span12 a-text-center')]//img[contains(@class,'s-access-image cfMarker')]").click() yes
	current_urls.append(str(driver.current_url))
	driver.back()
	driver.find_element_by_id("twotabsearchtextbox").clear()
driver.close()
'''
# items = ['B01KIQH2VU','B01B5ITZ4M']
for asin in items:
	review_list = []
	review_number = 0
	for page in range(1,3):
		html = requests.get('https://www.amazon.com/product-reviews/' + asin + '/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&reviewerType=all_reviews&filterByStar=five_star&pageNumber='+str(page),headers = {'User-Agent':'Mozilla/5.0'})
		soup = BeautifulSoup(html.text,"lxml")
		review = soup.find_all("span",{'data-hook':'review-body'})
		reviewertemp = soup.find_all("span",{'data-hook':'review-author'})
		for r in review:
			r = r.text
			review_list.append(r)
		print("processing:" + asin + " page:" + str(page))
		# print(html.url)
	print(asin," : ",html.url)
	for each in review_list:
		print(each.encode(encoding='UTF-8',errors='ignore'))
