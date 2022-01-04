import os,sys
import requests
from bs4 import BeautifulSoup
import time

def deal_html(url):
    try:
        html = requests.get(url)
    except requests.exceptions.ConnectionError:
        html.status_code = "Connection refused"

    if html.status_code == 200:
        soup = BeautifulSoup(html.text, "html.parser")
        print("connecting successed!")
        return soup
    else:
        return None

def getHTML(url):
    soup = deal_html(url)
    # web_base = "https://ywchuangyue.en.alibaba.com/prod"
    url_split_list = url.split("/")
    web_base = url_split_list[0] + "//" +url_split_list[2]
    html_list = []
    img_list = soup.find(name='div',attrs={'class':'component-product-list'}).find_all('a')
    print("img_list in getHTML 22line")
    for link in img_list:
        new_link = web_base + str(link.get('href'))
        html_list.append(new_link)  
    return html_list

def create_folder(dirs_dict):
    for each_dir,dir_path in dirs_dict.items():
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print("finished mkdir {}".format(dir_path))

def save_Img(url, apath ):
    html = requests.get(url)
    img_name = url.split("/")[-1].replace(" ", "_").replace(",","").replace("&","and")
    print(img_name)
    with open(apath + '/' + img_name, 'wb') as f:
        for chunk in html.iter_content(chunk_size=32):
            f.write(chunk)

def getImg(html, index, path):
    soup = deal_html(html)
    print(soup.text)
    #main_img_list   = soup.find(name='div', attrs={'class': 'scc-wrapper detail-module module-detailBoothImage'}).find_all('img')
    #detail_img_list = soup.find(name='div', attrs={'class': 'scc-wrapper detail-module module-productSpecification'}).find_all('img')
    print(soup.find(name="div",attrs={'class':'pc-main-image'}))
    #main_img_list = soup.find(name="div",attrs={'class':'pc-main-image'}).find_all('img')
    '''
    dirs  = {
            'output_dir' : path,
            'product_dir' : path + '/product_' + index,
            'detail_img_dir': path + '/product_' + index + '/detail_img',
            }
    create_folder(dirs)
    print(main_img_list)
    for link in main_img_list:
        url_link = link['src'].replace("_350x350.jpg","").replace("_50x50.jpg","")
        if not url_link.startswith("https:"):
            url_link = "https:" + url_link
        save_Img(url_link, dirs['product_dir'])
    for link in detail_img_list:
        url_link = link['src'].replace("_350x350.jpg","").replace("_50x50.jpg","")
        if not url_link.startswith("https:"):
            url_link = "https:" + url_link
        save_Img(url_link, dirs['detail_img_dir'])
    '''
def main():
    #url = "https://bestexltd.en.alibaba.com/productgrouplist-807760173/Leggings_Pants.html?spm=a2700.shop_pl.98.1"
    url = "https://ywchuangyue.en.alibaba.com/productgrouplist-806860118/Active_Leggings.html?spm=a2700.shop_pl.98.1"
    #https://diqian.1688.com/page/offerlist.htm?spm=a2615.2177701.autotrace-topNav.3.68b41735oBtMa4
    #url = input("input your html url here: ")
    html_list = getHTML(url)
    print("I get html list:")
    all_products = list(set(html_list))
    
    #outdir = input("all picture will download under this name : please input a new folder name:")
    outdir = "asd"
    for index, product_html in enumerate(all_products, start=1):
        index = str(index).zfill(3)
        print("{}: {}".format(index, product_html))
        getImg(product_html, index, outdir)
        time.sleep(1)

if __name__ == "__main__":
    main()
