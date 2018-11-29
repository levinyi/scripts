#-*-coding:utf-8 -*-
import urllib2
import lxml.html
import requests

def amazon_price(url, user_agent):
    kv = {'user-agent': user_agent}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    tree = lxml.html.fromstring(r.text.encode("utf-8"))
    price = tree.cssselect("span#priceblock_ourprice")[0]
    return price.text_content().encode("utf-8")

if __name__=="__main__": 
    url = "https://www.amazon.com/QUEEN-ROSE-Pregnancy-Pillow-Hypoallergenic/dp/B01M6YE2M8"
    user_agent = 'Mozilla/5.0'
    print amazon_price(url, user_agent)
