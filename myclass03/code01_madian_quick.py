#author:shapemind
#dt: 2021/12/14 10:16
import queue

"""
 * 【题目】——随时找到数据流的中位数
 * 有一个源源不断地吐出整数的数据流，假设你有足够的空间来保存吐出的数。请设计一个名叫MedianHolder的结构，MedianHolder可以
 * 随时取得之前吐出所有数的中位数。
 *
 * 【要求】
 * 1．如果MedianHolder已经保存了吐出的N个数，那么任意时刻将一个新数加入到MedianHolder的过程，其时间复杂度是O(logN)。
 * 2．取得已经吐出的N个数整体的中位数的过程，时间复杂度为O(1)。
"""
class MedianHolder:
	
	def __init__(self):
		self.max_heap = queue.PriorityQueue()
		self.min_heap = queue.PriorityQueue()
	
	def modify_two_heap_size(self):
		if self.max_heap.qsize() + 2 == self.min_heap.qsize():
			self.max_heap.put(self.min_heap)
	
	
def main():
	heap = queue.PriorityQueue()
	heap.put(1)
	heap.put(2)
	heap.put(3)
	heap.get()
	print(heap.qsize())
	
if __name__ == '__main__':
    main()