import requests
from time import sleep
import codecs

# url = "url-of-products"
# html = requests.get(url)

def getUA():
    with open("newUA.txt") as fileua:
        uas = fileua.readlines()
        import random
        cnt = random.randint(0,len(uas)-1)
        return uas[cnt].replace("\n","")

def getHeader(referer):
    header = {
        'Referer': referer,
        'User-agent': getUA(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accetp-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'en-US,en;q=0.8'
    }
    return header

def download_page(url, id, referer, header, cookie, pause):
    htmlpage = None
    while htmlpage is None:
        code = 404
        with requests.session() as s:
            html = s.get(url, headers=getHeader(referer), cookies = cookie)
            htmlpage = html.content.decode('utf-8','ignore')
            if not id in htmlpage:
                htmlpage = None
                continue
            code = html.status_code
            sleep(pause)
    if htmlpage:
        return htmlpage, code
    else:
        return None, code

def main():

# urlPart1 = "http://www.amazon.com/product-reviews/"
# urlPart2 = "/?ie=UTF8&reviewerType=all_reviews&pageNumber="
# url = urlPart1 + productID + urlPart2 + pageNumber
# html = requests.get(url)

    urlPart1 = "http://www.amazon.com/product-reviews/"
    urlPart2 = "/?ie=UTF8&reviewerType=all_reviews&pageNumber="

    id_ = "B00BUSDVBQ"
    pause = 0
    lastPage = 3

    referer = urlPart1 + str(id_) + urlPart2 + "1"
    header = getHeader(referer)
    # print header
    with requests.session() as s:
        req = s.get(referer, headers=header)
        cookie = requests.utils.dict_from_cookiejar(req.cookies)

    page = 1 
    while page <= lastPage:
        url = urlPart1 + str(id_) + urlPart2 + str(page)
        htmlpage, code = download_page(url,id_, referer, header, cookie, pause)

        with codecs.open(id_+'_'+str(page)+'.html',mode='w',encoding='utf8') as file:
            file.write(htmlpage)

        page += 1
        referer = urlPart1 + str(id_) + urlPart2 + str(page)
        with requests.session() as s:
            req = s.get(referer, headers=getHeader(referer))
            cookie = requests.utils.dict_from_cookiejar(req.cookies)

if __name__ == '__main__':
	main()