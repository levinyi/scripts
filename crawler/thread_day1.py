import threading
import time

def thread_job():
	# print("this is add_thread,number is %s"% threading.current_thread())
	print("T1 start\n")
	for i in range(10):
		time.sleep(0.1)
	print("T1 finish\n")

def T2_job():
	print("T2 start\n")
	print("T2 finish\n")
def main():
	add_thread=threading.Thread(target=thread_job,name="T1")
	thread2 = threading.Thread(target=T2_job,name="T2")
	add_thread.start()
	thread2.start()
	thread2.join()
	add_thread.join()
	# print(threading.active_count())
	# print(threading.enumerate())
	# print(threading.current_thread())
	print("all done\n")


if __name__ == '__main__':
	main()



