#author:shapemind
#dt: 2021/12/6 13:55
import os
import time
import random

def generate_code(code_len=4):
	all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	last_pos = len(all_chars) - 1
	code = ''
	for _ in range(code_len):
		index = random.randint(0, last_pos)
		code += all_chars[index]
	return code

def get_suffix(filename, has_dot=False):
	"""
	获取文件名后缀名
	:param filename:文件名
	:param has_dot: 返回后缀名是否需要带点
	:return: 文件名后缀
	"""
	pos = filename.rfind('.')
	if 0 < pos < len(filename) - 1:
		index = pos if has_dot else pos + 1
		return filename[index:]
	else:
		return ''
	
def max2(x):
	m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
	for index in range(2, len(x)):
		if (x[index] > m1):
			m2 = m1
			m1 = x[index]
		elif x[index] > m2:
			m2 = x[index]
	return m1, m2

def is_leap_year(year):
	"""
	判断指定年份是否为闰年
	:param year: 年份
	:return: 闰年返回True，平年返回False
	"""
	return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month,date):
	"""
	计算传入的日期是这一年的第几天
	:param year: 年
	:param month: 月
	:param date: 日
	:return: 是一年中的第几天
	"""
	days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
	return days_of_month
	# total = 0
	# for index in range(month - 1):
	# 	total += days_of_month[index]
	# return total + date
def main():
	# 字面量创建字典 | 输出{'捷祖': 100, '冬冬': 98, '尹天仇': 50}
	score = {'捷祖': 100, '冬冬': 98, '尹天仇': 50}
	# print(score)
	# # 构造器创建字典 | 输出{'one': 1, 'two': 2, 'three': 3, 'four': 4}
	# item = dict(one=1, two=2, three=3, four=4)
	# print(item)
	# # 构造器中使用zip拉链构建字典 | 输出{'a': '1', 'b': '2', 'c': '3'}
	# item2 = dict(zip(['a', 'b', 'c'], '123'))
	# print(item2)
	# # 推倒式语法创建字典 | 输出{1: 1, 2: 4, 3: 9, 4: 16}
	# item3 = {num : num ** 2 for num in range(1, 5)}
	# print(item3)
	
	# # 查找字典元素 | 输出98
	# print(score['冬冬'])
	# print(score.get('冬冬')) #score.get()犹豫score[],当key不存在时score[]报错
	# if '冬冬' in score:
	# 	print(score['冬冬'])
	# # 遍历字典元素 | 输出捷祖 : 100 冬冬 : 98 尹天仇 : 50
	# for key in score:
	# 	print(f'{key} : {score[key]}', end=' ')
	# print()
	# # 更新字典元素
	# score['冬冬'] = 99 #输出{'捷祖': 100, '冬冬': 99, '尹天仇': 50}
	# score['浑天元'] = 0 #当找不到key时，则是加入此键值对 | 输出{'捷祖': 100, '冬冬': 99, '尹天仇': 50, '浑天元': 0}
	# score.update(天鹅=8,捷祖=50) #存在键值对更新，不存在加入 | 输出{'捷祖': 50, '冬冬': 99, '尹天仇': 50, '浑天元': 0, '天鹅': 8}
	# print(score.get('春春', 60)) #若查找值不在，则返回默认值 |　输出60
	# # 删除字典元素
	# print(score.popitem()) #从后往前删除 | 输出('天鹅', 8)
	# print(score.pop('冬',999)) #弹出指定key的键值对 | 输出999
	# # 清空字典
	# score.clear()
	# content = '北京欢迎你~'
	# while True:
	# 	os.system('clear')
	# 	print(content)
	# 	time.sleep(1)
	# 	content = content[1:] + content[0]
	# list1 = [2,3,5,6,1,6,7,1]
	# print(max2(list1))
	# print(which_day(2001,1,1))
	num = int(input('Number of rows: '))
	yh = [[]] * num # [[],[],[],[],[]]
	for row in range(len(yh)):
		yh[row] = [None] * (row + 1)
		print(yh[row])
		for col in range(len(yh[row])):
			if col == 0 or col == row:
				yh[row][col] = 1
			else:
				yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
			print(yh[row][col], end='\t')
		print()

if __name__ == '__main__':
	main()