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
def main():
    # 生成式：创建列表，列表创建后元素就绪，因而消耗内存空间 | 输出[0, 1, 2, 3, 4]
    list1 = [x for x in range(5)]
    # 输出['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
    list2 = [x + y for x in 'ABC' for y in '12']
    # getsizeof()，查看对象占用内存字节数 | 输出68
    print(sys.getsizeof(list2))
    
    # 生成器：创建生成器非列表，能节省内存空间，但计算时要重新加载到内容，耗费时间变长
    creator = (x ** 2 for x in range(3))
    # 输出<generator object main.<locals>.<genexpr> at 0x01F423B0>内存地址
    print(creator)
    # 输出64
    print(sys.getsizeof(creator))
    # 打印生成器元素 | 输出0 1 4
    for creatorer in creator:
        print(creatorer,end=' ')

if __name__ == '__main__':
    main()