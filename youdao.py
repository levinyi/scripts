#! -- coding=utf-8 --
import requests
from lxml import etree

url = "http://m.youdao.com/translate"
headers = {
    'User-Agent':
    'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5 MIUI/V8.1.6.0.MAACNDI)'
}
data_list = ["我来自美丽的中国", "完美", "beautiful", "Nice to meet you too"]
for data in data_list:
    data = {"inputtext": data, "type": "AUTO"}
    con = requests.post(url, data).content.decode("utf8")
    html = etree.HTML(con)
    res = html.xpath("//ul[@id='translateResult']/li/text()")
    print(res)
