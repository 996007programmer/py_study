#author:shapemind
#dt: 2021/12/11 17:20

class Student(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def study(self, course_name):
		print('%s正在学习%s.' % (self.name, course_name))
		
	def watch_movie(self):
		if self.age < 18:
			print('%s只能观看《熊出没》' % self.name)
		else:
			print('%s正在观看岛国爱情大电影.' % self.name)
	
class Test:
	def __init__(self, foo):
		self.__foo = foo
		
	def __bar(self):
		print(self.__foo)
		print('__bar')

class Clock(object):
	"""数字时钟"""
	
	def __init__(self, hour=0, minute=0, second=0):
		"""
		初始化方法
		:param hour:时
		:param minute:分
		:param second: 秒
		"""
		self.hour = hour
		self.minute = minute
		self.second = second
	
	def run(self):
		"""走法"""
		self.second += 1
		if self.second == 60:
			self
			
def main():
	stu1 = Student('冬冬', 24)
	stu1.study('Python程序设计')
	stu1.watch_movie()
if __name__ == '__main__':
	test = Test('hello')
	test._Test__bar()
	print(test._Test__foo)