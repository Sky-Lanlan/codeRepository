import threading
import time

list = []

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        # threadLock.acquire()
        add_counter(self.name,self.threadID,self.counter)
        # 释放锁，开启下一个线程
        # threadLock.release()

def add_counter(threadName,num,counter):
	while counter:
		list.append(num)
		print (threadName)
		print(list)
		counter -=1
        

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 4)
thread2 = myThread(2, "Thread-2", 4)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
