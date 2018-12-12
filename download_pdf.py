import requests
from bs4 import BeautifulSoup

url = "https://openstax.org/details/books/biology"
'''
headers = {
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection' : 'Keep-Alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
html = requests.get(url,headers = headers)
print(html.text)
soup = BeautifulSoup(html.text,"lxml")
print(soup.select('a'))
'''

from selenium import webdriver  
# driver = webdriver.Chrome('/cygene/script/test/chromedriver')
driver = webdriver.PhantomJS('/cygene/software/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.get(url)
print(driver.current_url)
page = requests.get(driver.current_url,headers={'User-Agent':'Mozilla/5.0'})
print(page.text)


'''
if html.status_code == 200:
    # print "yes"
    soup = BeautifulSoup(html.text, "html.parser")
    # print soup.p
    # print soup.a
    # print soup.body
    print soup.select("div class")

    print soup.find_all("span")
    print soup.find_all("scripts")


import urllib2

response = urllib2.urlopen(url)
print response.read()
'''