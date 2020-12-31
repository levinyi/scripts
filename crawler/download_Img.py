import os
import requests



def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r"img src='(.+?\.jpg)'"
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist

url = "https://bestexltd.en.alibaba.com/productgrouplist-807760173/Leggings_Pants.html?spm=a2700.shop_pl.98.1"
html = getHtml(url)
for imgurl in getImg(html):
    urllib.urlretrieve(imgurl, "./")
