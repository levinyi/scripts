import requests
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
# url = "https://movie.douban.com/top250"

def db(page):
    num = (page -1) *25
    url = 'https://movie.douban.com/top250?start='+str(num)
    res = requests.get(url, headers=headers).text
    p_title = '<img width="100" alt="(.*?)"'
    title = re.findall(p_title, res)
    p_img = '<img width="100" alt=".*?" src="(.*?)"'
    img = re.findall(p_img, res)

    for i in range(len(title)):
        print(str(i + 1)+'.'+title[i])
        print(img[i])
        res = requests.get(img[i])
        file = open('images/'+title[i] +'.jpg', 'wb')
        file.write(res.content)
        file.close()

for i in range(10):
    db(i +1)
    print('第'+ str(i+1) +'页爬取成功')