from typing import List
class solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        for i in range(lens):
            num1 = nums[i]
            num2 = target - num1
            if num2 in nums:
                if num1 == num2 and not nums.count(num1) > 1:
                    continue
                return [i, nums.index(num2, i+1)]

def main():
    solution1 = solution()
    list2 = solution1.twosum([1, 2, 3, 4], 7)
    print(list2)

if __name__ == '__main__':
    main()
