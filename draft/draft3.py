#author:shapemind
#dt: 2021/12/6 11:06

def main():
	set1 = {1, 2, 3, 4}
	set2 = {3, 4, 5}
	
	# 交集 | 输出{3, 4}
	print(set1 & set2)
	print(set1.intersection(set2))
	# 并集 | 输出{1, 2, 3, 4, 5}
	print(set1 | set2)
	print(set1.union(set2))
	# 差集 | 输出{1, 2}
	print(set1 - set2)
	print(set1.difference(set2))
	# 并集 - 交集 = (set1 | set2) - (set1 & set2) | 输出{1, 2, 5}
	print(set1 ^ set2)
	
	# 判断子集 | 输出False
	print(set2 <= set1)
	print(set2.issubset(set1))
	# 判断超集 | 输出False
	print(set2 >= set1)
	print(set2.issuperset(set1))
	
if __name__ == '__main__':
	main()