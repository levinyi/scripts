import threading
import time

tlock = threading.Lock()

def timer(name,delay,repeat):
	print("Timer: "+ name + "started")
	tlock.acquire()
	print(name + "Has acquired the lock")
	while repeat >0:
		time.sleep(delay)
		print(name + ": " + str(time.ctime(time.time())))
		repeat -=1
	print(name +" is releasing the lock")
	tlock.release()
	print("Timer: "+name + " Completed")

def Main():
	t1 = threading.Thread(target=timer,args=("Timer1",1,5))
	t2 = threading.Thread(target=timer,args=("Timer2",2,5))
	t1.start()
	t2.start()
	print("Main completed")

if __name__ == '__main__':
	Main()


##############################
'''
class AsyncWrite(threading.Thread):
	"""docstring for AsyncWrite"""
	def __init__(self, text,out):
		self.text = text
		self.out = out

	def run(self):
		f = open(self.out,"a")
		f.write(self.text + '\n' )
		f.close()
		time.sleep(2)
		print("finished background file write to " + self.out)

def Main():
	message = input("Enter a sting to store:")
	background = AsyncWrite(message,'out.txt')
	background.start()
	print("the program can continue while it write in anthre thread")
	print("100+400=500")
	background.join()
	print ("waited until thread was conplete")

if __name__ == '__main__':
	Main()
'''		