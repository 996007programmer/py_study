#author:shapemind
#dt: 2021/12/15 10:59
from random import randint
from time import time
from functools import lru_cache
def swap(list, i, j):
	tmp = list[i]
	list[i] = list[j]
	list[j] = tmp

def partiton(list, l, r):
	less = l - 1
	more = r
	while l < more:
		if list[l] < list[r]:
			less+=1
			swap(list, less, l)
			l+=1
		elif list[l] > list[r]:
			more-=1
			swap(list, more, l)
		else:
			l+=1
	swap(list, more, r)
	return [less + 1, more]
@lru_cache(maxsize=1000000, typed=True)
def mini_quicksort(list, l, r):
	if l < r:
		swap(list, l + randint(0, r - l), r)
		p = partiton(list, l, r)
		mini_quicksort(list,0,p[0] - 1)
		mini_quicksort(list,p[1] + 1, r)
		
def quicksort(list):
	if list is None or len(list) < 2:
		return
	
	mini_quicksort(list, 0, len(list) - 1)


def generate_list(max_size, max_value):
	list = []
	list_length = randint(0, max_size)
	for _ in range(list_length):
		append_number = randint(0, max_value) -randint(0, max_value + 1)
		list.append(append_number)
	return list


def copyArray(list):
	return list.copy()

def comparator(list):
	list.sort()

def main():
	max_size = 100
	max_value = 200
	test_time = 1
	is_succeed = True
	list1 = generate_list(max_size, max_value)
	list2 = list1.copy()
	print(list1)
	print(list2)
	quicksort(list1)
	print(list1)
	# comparator(list2)
	# print(list2)
	# start_time = time()
	# for _ in range(test_time):
	# 	list1 = generate_list(max_size, max_value)
	# 	list2 = copyArray(list1)
	# 	quicksort(list1)
	# 	comparator(list2)
	# 	if not (list1 == list2):
	# 		is_succeed = False
	# 		print(list1)
	# 		print(list2)
	# 		break
	# end_time = time()
	# print('总耗时%.3f' % (end_time - start_time)) if is_succeed else print('Fucking fucked!')
if __name__ == '__main__':
    main()