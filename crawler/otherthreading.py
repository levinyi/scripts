# coding:utf-8
import threading
import time
import random

class Producer(threading.Thread):
	"""docstring for Producer"""
	def __init__(self, integers,condition):
		self.integers = integers
		self.condition = condition
		
	def run(self):
		while True:
			integers = random.randint(0,256)
			self.condition.acquire() # 获取锁
			print ('生产者{}正在获取锁'.format(self.name))
			self.integers.append(integers)
			print ('生产者{}生产了一个随机数{}把它加入到list里面'.format(self.name,integers))
			self.condition.notify() # 唤醒消费者
			self.condition.release()
			time.sleep(2)

class Consumer(threading.Thread):
	"""docstring for Consumer"""
	def __init__(self, integers,condition):
		self.integers = integers
		self.condition = condition
	def run(self):
		while True:
			self.condition.acquire()
			while True:
				if self.integers:
					integers = self.integers.pop()
					print ("消费者{}消费了一个随机数{}".format(self.name,integers))
					break
				print ('消费者{}准备消费，但是没有资源，于是等待生产'.format(self.name))
				self.condition.wait() # 等待并且释放锁
			self.condition.release()
			time.sleep(2)

def main():
	integers=[]
	condition = threading.Condition()
	for i in range(5):
		t = Producer(integers,condition)
		t.start()
	for i in range(5):
		t = Consumer(integers,condition)
		t.start()

if __name__ == '__main__':
	main()

