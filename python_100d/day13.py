#author:shapemind
#dt: 2021/12/15 16:34
"""
from time import sleep
from threading import Thread, Lock

class Account(object):
	
	def __init__(self):
		self._balance = 0
		self._lock = Lock()
		
	def deposit(self, money):
		#需要获得锁才可以继续下面操作
		self._lock.acquire()
		try:
			new_balance = self._balance + money
			sleep(0.01)
			self._balance = new_balance
		finally:
			# finally确保不管是什么情况都能正常释放锁
			self._lock.release()
		
	@property
	def balance(self):
		return self._balance

class AddMoneyThread(Thread):
	
	def __init__(self, account, money):
		super().__init__()
		self._account = account
		self._money = money
	
	def run(self):
		self._account.deposit(self._money)

def main():
	account = Account()
	threads = []

	for _ in range(100):
		t = AddMoneyThread(account, 1)
		threads.append(t)
		t.start()
	for t in threads:
		t.join()
	print('账户余额为：￥%d元' % account.balance)
"""

from multiprocessing import Process, Queue
from time import time
from random import randint

def task_handler(curr_list, result_queue):
	total = 0
	for number in curr_list:
		total += number
	result_queue.put(total)

def main():
	processes = []
	number_list = [x for x in range(1,10000001)]
	result_queue = Queue()
	index = 0
	count = 0
	for _ in range(8):
		p = Process(target=task_handler, args=(number_list[index: index + 1250000], result_queue))
		index += 1250000
		processes.append(p)
		count += 1
	
	start_time = time()
	count = 0
	count2 = 0
	for p in processes:
		p.start()
		print('start', count2)
		count2 += 1
		p.join()
		print('下面',count)
		count += 1
	total = 0
	while not result_queue.empty():
		total += result_queue.get()
	print(total)
	end_time = time()
	print('Execution time: ', (end_time - start_time), 's', sep='')
	
if __name__ == '__main__':
    main()