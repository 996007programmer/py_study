#author:shapemind
#dt: 2021/12/15 14:20
import re

def main():
	# match，判断是否匹配 | 输出<re.Match object; span=(0, 10), match='liangjiezu'>
	username = """liangjiezu"""
	m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
	print(m1)
	
	# split, 裂开 | 输出['liang', 'iezu']
	list1 = re.split(r'j',username)
	print(list1)
	# sub，替换 | 输出liangJiezu
	username2=re.sub(r'j', 'J', username)
	print(username2)
	# fullmatch | 输出<re.Match object; span=(0, 10), match='liangjiezu'>
	# 参数列表的re.I表示忽略大小写
	fullmatch_flag = re.fullmatch(r'liangjiezu',username, re.I)
	print(fullmatch_flag)
	# compile,创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
	pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
	sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，不是15600998765，不是15600998765，也不是110或119，王大锤的手机号才是15600998765。
	   '''
	# findall, 查找所有匹配并保存到一个列表中 | 输出['13512346789', '15600998765', '15600998765', '15600998765']
	mylist = re.findall(pattern, sentence)
	print(mylist)
	
	# finditer,通过迭代器取出匹配对象并获得匹配的内容，
	# 当pattern = re.compile(r'([0-9]*)([a-z]*)([0-9]*)')时，group(1)表示取满足正则表达式要求的字符串的([a-z]*)部分
	# 输出13512346789\n 15600998765\n 15600998765\n 15600998765
	for temp in pattern.finditer(sentence):
		print(temp.group())
		
	# search
	print('~~~~~~~分割线~~~~~~~~')
	m = pattern.search(sentence)
	while m:
		print(m.group())
		# search(sentence, m.end()) 意思从找到的m的最后一个字符串的位置开始查找，若少了这个，就会反复一直查找
		m = pattern.search(sentence, m.end())
	
	# purge(),清楚缓存
	re.purge()

if __name__ == '__main__':
    main()