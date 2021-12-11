#author:shapemind
#dt: 2021/12/6 13:55
import os
import time
from random import randrange, randint, sample
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
	total = 0
	for index in range(month - 1):
		total += days_of_month[index]
	return total + date


def display(balls):
	"""
	输出列表中的双色球号码
	:param balls:
	:return: 无返回
	"""
	for index, ball in enumerate(balls):
		if index == len(balls) - 1:
			print('|')
		print('%02d' % ball, end=' ')
	print()


def random_select():
	"""
	随机选择一组号码
	:return: 返回一个列表
	"""
	red_balls = [x for x in range(1, 34)]
	selected_balls = []
	selected_balls = sample(red_balls, 6)
	selected_balls.sort()
	selected_balls.append(randint(1, 16))
	return selected_balls


	
# def main():
# 	persons = [True] * 30
# 	counter, index, number = 0, 0, 0
# 	while counter < 15:
# 		if persons[index]:
# 			number += 1
# 			if number == 9:
# 				persons[index] = False
# 				counter += 1
# 				number = 0
# 		index += 1
# 		index %= 30
# 	for person in persons:
# 		print('基' if person else '非',end='')

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
	main()