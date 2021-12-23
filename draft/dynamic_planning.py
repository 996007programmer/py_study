#author:shapemind
#dt: 2021/12/23 19:43
from typing import List

def L(nums: List[int], i: int) -> int:
	""" Returns the length of longest increasing subsequence starting from i"""
	
	if i == len(nums) - 1:
		return 1
	
	max_len = 1
	for j in range(i + 1, len(nums)):
		if nums[j] > nums[i]:
			max_len = max(max_len, L(nums, j) + 1)
	return max_len

def length_of_LIS(nums: List[int]):
	return max(L(nums, i) for i in range(len(nums)))

def main():
	nums = [1,5,2,4,3]
	print(length_of_LIS(nums))

if __name__ == '__main__':
    main()