#author:shapemind
#dt: 2021/12/1 15:07

# row = int(input('请输入行数:'))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*',end='')
#     print()
    
# row1 = int(input('请输入行数：'))
# for i in range(row1):
#     for j in range(row1):
#         if j < row1 - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

# row2 = int(input('请输入打印行数3：'))
# for i in range(row2):
#     for _ in range(row2 - i - 1):
#         print(' ',end='')
#     for _ in range(2 * i + 1):
#         print('*',end='')
#     print()
import sys


def find_power_number():
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)



def craps_game():
    from random import randint
    
    money = 1000
    while money > 0:
        print('你的总资产为:', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注: '))
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜')
                money -= debt
            elif current == first:
                print('玩家胜')
                money += debt
            else:
                needs_go_on = True
    print('你破产了, 游戏结束!')
    
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        print(factor,end=' ')
        
def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数

def foo():
    a = 100
    def koo():
        nonlocal a
        a += 1
    koo()
    

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a
        
def main():
    for val in fib(20):
        print(val, end=' ')

if __name__ == '__main__':
    main()