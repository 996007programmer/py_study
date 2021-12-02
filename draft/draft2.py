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

row2 = int(input('请输入打印行数3：'))
for i in range(row2):
    for _ in range(row2 - i - 1):
        print(' ',end='')
    for _ in range(2 * i + 1):
        print('*',end='')
    print()
    
def find_power_number:
