#author:shapemind
#dt: 2021/12/11 14:56
from random import randint


def swap(list, i, j):
	list[i] = list[i] ^ list[j]
	list[j] = list[i] ^ list[j]
	list[i] = list[i] ^ list[j]


def bubblesort(list):
	# 判断是否异常
	if list == None or len(list) < 2:
		return
	
	for e in range(len(list) - 1, 0, -1):
		for i in range(e):
			if (list[i] > list[i + 1]):
				swap(list, i, i + 1)

def comparator(list):
	list.sort()
	
def generate_random_list(max_size, max_value):
	list = [None] * randint(0, max_size + 1)
	for i in range(len(list)):
		list[i] = randint(0, max_value + 1) - randint(0, max_value)
	
	return list
def copy_list(list):
	if list == None:
		return
	
	list_copy = [None] * len(list)
	for i in range(len(list_copy)):
		list_copy[i] = list[i]
	
	return list_copy

def isequal(list1, list2):
	if (list1 == None and list2 != None) or (list1 != None and list2 == None) or (len(list1) != len(list2)):
		return False
	if list1 == None and list2 == None:
		return True
	for i in range(len(list1)):
		if(list1[i] != list2[i]):
			return False
			break
	
	return True

def main():
	test_time, max_size, max_value = 50000, 100, 200
	all_isequal = True
	for _ in range(test_time):
		list1 = generate_random_list(max_size, max_value)
		list2 = copy_list(list1)
		bubblesort(list1)
		comparator(list2)
		if not isequal(list1, list2):
			all_isequal = False
			print('list1:',list1)
			print('list2:',list2)
			break
	
	print('Nice!') if all_isequal else print('Fucking fucked!')
	
if __name__ == '__main__':
	main()