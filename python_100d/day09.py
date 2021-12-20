# author:shapemind
# dt: 2021/12/14 14:06
# class Person(object):
#
# 	def __init__(self, name, age):
# 		self._name = name
# 		self._age = age
#
# 	#访问器 - getter方法
# 	@property
# 	def name(self):
# 		return self._name
# 	#访问器 - getter方法
# 	@property
# 	def age(self):
# 		return self._age
#
# 	#修改器 - setter方法
# 	@name.setter
# 	def name(self, name):
# 		self._name = name
# 	#修改器 - setter方法
# 	@age.setter
# 	def age(self, age):
# 		self._age = age
from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
	"""战斗属性"""
	__slots__ = ('_name', '_hp')
	
	def __init__(self, name, hp):
		self._name = name
		self._hp = hp
	
	@property
	def name(self):
		return self._name
	
	@property
	def hp(self):
		return self._hp
	
	@hp.setter
	def hp(self, hp):
		self._hp = hp if hp >= 0 else 0
	
	@property
	def alive(self):
		return self._hp > 0
	
	@abstractmethod
	def attack(object, other):
		"""攻击"""
		pass


class Ultraman(Fighter):
	"""奥特曼"""
	__slots__ = ('_name', '_hp', '_mp')
	
	def __init__(self, name, hp, mp):
		super().__init__(name, hp)
		self._mp = mp
	
	def attack(object, other):
		other.hp -= randint(15, 25)
	
	def huge_attack(self, others):
		if self._mp >= 20:
			self._mp -= 20
			for temp in others:
				if temp.alive:
					temp.hp -= randint(10, 15)
			return True
		else:
			return False
	
	def resume(self):
		incr_point = randint(1, 10)
		self._mp += incr_point
		return incr_point
	
	def __str__(self):
		return '~~~%s奥特曼~~~' % self._name + \
		       '生命值：%s' % self._hp + \
		       '魔法值：&s' % self._mp


class Monster(Fighter):
	"""怪兽"""
	__slots__ = ('_name', '_hp')
	
	def attack(object, other):
		other.hp -= randint(10, 20)
	
	def __str__(self):
		return '~~~%s小怪兽~~~\n' % self._name + '生命值：%d\n' % self._hp


def is_any_alive(monsters):
	for monster in monsters:
		if monster.alive > 0:
			return True
	return False


def select_alive_one(monsters):
	monsters_len = len(monsters)
	while True:
		index = randrange(-1, monsters_len)
		monster = monsters[index]
		if monster.alive > 0:
			return monster


def display_info(ultramans, monsters):
	"""显示奥特曼和小怪兽的信息"""
	print(ultramans)
	for monster in monsters:
		print(monster, end='')


class PersonSlot(object):
	# 限定PersonSlot对象只能绑定_name，_age，_gender属性
	__slots__ = ('_name', '_age', '_gender')
	
	def __init__(self, name, age):
		self._name = name
		self._age = age
	
	@property
	def name(self):
		return self._name
	
	@property
	def age(self):
		return self._age
	
	@name.setter
	def name(self, name):
		self._name = name
	
	@age.setter
	def age(self, age):
		self._age = age


class Triangle(object):
	def __init__(self, a, b, c):
		self._a = a
		self._b = b
		self._c = c
	
	@staticmethod
	def is_valid(a, b, c):
		return a + b > c and b + c > a and a + c > b


"""
类方法
"""


class Clock(object):
	def __init__(self, hour=0, minute=0, second=0):
		self._hour = hour
		self._minute = minute
		self._second = second
	
	@classmethod
	def now(cls):
		from time import time, localtime, sleep
		ctime = localtime(time())
		return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
	
	def show(self):
		return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


class Person(object):
	def __init__(self, name, age):
		self._name = name
		self._age = age
	
	@property
	def name(self):
		return self._name
	
	@property
	def age(self):
		return self._age
	
	@name.setter
	def name(self, name):
		self._name = name
	
	@age.setter
	def age(self, age):
		self._age = age


class Student(Person):
	def __init__(self, name, age, grade):
		super().__init__(name, age)
		self._grade = grade
	
	@property
	def grade(self):
		return self._grade
	
	@grade.setter
	def grade(self, grade):
		self._grade = grade


class Teacher(Person):
	def __init__(self, name, age, title):
		super().__init__(name, age)
		self._title = title
	
	@property
	def title(self):
		return self._title
	
	@title.setter
	def title(self, title):
		self._title = title


from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
	"""宠物"""
	
	def __init__(self, nickname):
		self._nickname = nickname
	
	@abstractmethod
	def make_voice(self):
		"""发出声音"""
		pass


class Dog(Pet):
	"""狗"""
	
	def make_voice(self):
		print('%s：汪汪汪' % self._nickname)


class Cat(Pet):
	"""猫"""
	
	def make_voice(self):
		print('%s:喵喵喵~~' % self._nickname)


def main():
	u = Ultraman('骆昊', 1000, 120)
	m1 = Monster('狄仁杰', 250)
	m2 = Monster('白元芳', 500)
	m3 = Monster('王大锤', 750)
	ms = [m1, m2, m3]
	fight_round = 1
	while u.alive and is_any_alive(ms):
		print('========第%02d回合========' % fight_round)
		m = select_alive_one(ms)  # 选中一只小怪兽
		skill = randint(1, 10)  # 通过随机数选择使用哪种技能
		if skill <= 6:  # 60%的概率使用普通攻击
			print('%s使用普通攻击打了%s.' % (u.name, m.name))
			u.attack(m)
			print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
		elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
			if u.magic_attack(ms):
				print('%s使用了魔法攻击.' % u.name)
			else:
				print('%s使用魔法失败.' % u.name)
		else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
			if u.huge_attack(m):
				print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
			else:
				print('%s使用普通攻击打了%s.' % (u.name, m.name))
				print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
		if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
			print('%s回击了%s.' % (m.name, u.name))
			m.attack(u)
		display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
		fight_round += 1
	print('\n========战斗结束!========\n')
	if u.alive > 0:
		print('%s奥特曼胜利!' % u.name)
	else:
		print('小怪兽胜利!')
	
	print()


if __name__ == '__main__':
	main()
