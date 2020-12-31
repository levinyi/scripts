import itchat
import time
import requests

# itchat.auto_login()
# itchat.send('Hello, filehelper', toUserName='filehelper')


def get_news():
	# url = "http://open.iciba.com/dsapi"
	url = "http://news.iciba.com/dailysentence/tags-4.html"
	r = requests.get(url)
	contents = r.join()['content']
	translation = r.join()['translation']
	print (contents,translation)
	return contents,translation

def send_news():
	try:
		itchat.auto_login(hotReload=True)
		my_friend = itchat.search_friends(name=u'11°限量')
		print (my_friend)
		xiaoming = my_friend[0]['UserName']
		print ("xiaoming:",xiaoming)
		print("get_news:")
		message1 = str(get_news()[0])
		print('this is message1:',message1)
		content = str(get_news()[1][17:])
		message2 = str(content)
		itchat.send(message1,toUserName=xiaoming)
		itchat.send(message2,toUserName=xiaoming)
		t = time(5,send_news())
		t.start()
	except:
		message4 = u'some bug'
		itchat.send(message4,toUserName=xiaoming)


if __name__ == '__main__':
	send_news()