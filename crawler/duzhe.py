#!/usr/bin/python3
# coding:utf-8

import urllib2
import os
from bs4 import BeautifulSoup

def urlBS(url):
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	return soup

def main(url):
	soup = urlBS(url)
	link = soup.select('.booklist a')
	# path = os.getcwd+u'//'

	for item in link:
		newurl = baseurl +item['href']
		result = urlBS(newurl)
		title = result.find("h1").string
		writer = result.find(id="pub_date").string.strip()
		filename = path +title+'.txt'
		print(filename.encode("gbk"))
		new = open(filename,"w")
		new.write("<<"+ title.encode("gbk") + ">>\n\n")
		new.write(writer.encode("gbk")+"\n\n")
		text = result.select('.blkContainerSblkCon p')
		for p in text:
			context = p.txt
			new.write(context.encode("gbk"))
			pass
		new.close()

if __name__ == '__main__':
	time = '2015_03'
	baseurl = 'http://www.52duzhe.com/' + time +'/'
	firsturl = baseurl+'index.html'
	main(firsturl)