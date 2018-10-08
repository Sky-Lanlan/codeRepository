import _thread
import time
def print_time( threadName, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count +=1
		print("%s:%s"%(threadName,time.ctime(time.time())))


try:
	_thread.start_new_thread(print_time,("Thread-1",2,))
	_thread.start_new_thread(print_time,("Thread-2",4,))
except:
	print("Error: unable to start thread")
	
while 1:
	pass

import threading
import time

exitFlag = 0
class myThread(threading.Thread):
	def __init__(self,threadId,threadName,counter):
		threading.Thread.__init__(self)
		self.threadId = threadId
		self.threadName = threadName
		self.counter = counter
			
	def run(self):
		print("开始线程:"+self.threadName)
		print_time(self.threadName,self.counter,5)
		print("退出线程:"+self.threadName)

def print_time(threadName,delay,counter):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print(threadName+time.asctime(time.localtime()))
		counter -=1

thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",1.5)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")
