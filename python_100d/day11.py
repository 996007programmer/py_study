#author:shapemind
#dt: 2021/12/14 18:57
from math import sqrt
import json
def is_prime(n):
	"""
	判断是否为素数的函数
	:param n: 要判断的数字
	:return: 无返回
	"""
	assert n > 0
	for factor in range(2, int(sqrt(n)) + 1):
		if n % factor == 0:
			return False
	return True if n != 1 else False

def main():
	# filenames = ('a.txt', 'b.txt', 'c.txt')
	# fs_list = []
	# try:
	# 	for filename in filenames:
	# 		#open()会产生一个对象，所以此时fs_list里面一共有三个对象
	# 		fs_list.append(open(filename, 'w', encoding='utf-8'))
	# 	for number in range(1, 1000):
	# 		if is_prime(number):
	# 			if number < 100:
	# 				fs_list[0].write(str(number) + '\t')
	# 			elif number < 1000:
	# 				fs_list[1].write(str(number) + '\t')
	# 			else:
	# 				fs_list[2].write(str(number) + '\t')
	# except IOError as err:
	# 	print(err)
	# 	print('写文件时发生错误！')
	# finally:
	# 	for fs in fs_list:
	# 		fs.close()
	# print('操作完成')
	# try:
	# 	# 读取二进制文件
	# 	with open('graph.png','rb') as g1:
	# 		data = g1.read()
	# 		# type() 获取data类型 | 输出<class 'bytes'>
	# 		print(type(data))
	# 	# 写入二进制文件
	# 	with open('graph3.jpg','wb') as g2:
	# 		g2.write(data)
	# except FileNotFoundError as e:
	# 	print(e)
	# 	print('文件无法打开')
	# except IOError as e:
	# 	print('读写文件时出现错误')
	# print('程序执行结束')
	mydict = {
		'name': '骆昊',
		'age': 38,
		'qq': 957659,
		'friends': ['王大锤', '白元芳'],
		'car': [
			{'brand': 'BYD', 'max_speed': 180},
			{'brand': 'Audi', 'max_speed': 280},
			{'brand': 'Benz', 'max_speed': 320},
		]
	}
	try:
		with open('data1.json', 'w', encoding='utf-8') as fs:
			a = json.dumps(mydict, ensure_ascii=False)
			print(a)
			# json.dump(mydict, fs)
	except IOError as e:
		print(e)
	print('保存数据完成！')
if __name__ == '__main__':
    main()