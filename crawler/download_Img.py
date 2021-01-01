import os,sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def deal_html(url):
    try:
        html = requests.get(url)
    except requests.exceptions.ConnectionError:
        html.status_code = "Connection refused"

    if html.status_code == 200:
        soup = BeautifulSoup(html.text, "html.parser")
        return soup
    else:
        return NULL

def getHTML(url):
    soup = deal_html(url)
    html_list = []
    img_list = soup.find(name='div',attrs={'class':'component-product-list'}).find_all('a')
    for link in img_list:
        new_link = "https://bestexltd.en.alibaba.com" + str(link.get('href'))
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
    main_img_list   = soup.find(name='div', attrs={'class': 'scc-wrapper detail-module module-detailBoothImage'}).find_all('img')
    detail_img_list = soup.find(name='div', attrs={'class': 'scc-wrapper detail-module module-productSpecification'}).find_all('img')
    dirs  = {
            'output_dir' : path,
            'product_dir' : path + '/product_' + index,
            # 'main_img_dir': path + '/product_' + index + '/main_img', 
            'detail_img_dir': path + '/product_' + index + '/detail_img',
            }
    create_folder(dirs)

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

def main():
    url = "https://bestexltd.en.alibaba.com/productgrouplist-807760173/Leggings_Pants.html?spm=a2700.shop_pl.98.1"
    html_list = getHTML(url)
    all_products = list(set(html_list))
    outdir = sys.argv[1]
    for index, product_html in enumerate(all_products, start=1):
        index = str(index).zfill(3)
        print("{}: {}".format(index, product_html))
        getImg(product_html, index, outdir)

if __name__ == "__main__":
    main()
