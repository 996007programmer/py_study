#author:shapemind
#dt: 2021/12/23 9:35
from typing import List

""" 使用set判断 """
def contains_duplicate1(nums: List[int]) -> bool:
	if nums == None or len(nums) < 2:
		return False
	
	numset = set()
	for i in range(len(nums)):
		if nums[i] in numset:
			return True
		else:
			numset.add(nums[i])
	
	return False

""" 使用len()进行判断，不是很快，但是很简洁 """
def contains_duplicate2(nums: List[int]) -> bool:
	if nums == None or len(nums) < 2:
		return False
	
	return len(nums) != len(set(nums))

def comparator(nums: List[int]) -> bool:
	if nums == None or len(nums) < 2:
		return False
	
	for i in range(len(nums)):
		for j in range(len(nums)):
			if nums[i] == nums[j]:
				if i != j:
					return True
				
	return False

	
def main():
	flag = comparator([1,2,4,4,5])
	print(flag)


if __name__ == '__main__':
    main()