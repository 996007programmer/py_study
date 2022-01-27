# shapemind
import os

def main():
    
    # upper_name_list = os.listdir('D:\projects\\features')
    # name_list = []
    #
    # for name in upper_name_list:
    #     name_list.append(name.replace('.fql','.txt').lower())
    #
    # for name in name_list:
    #     print(name)
    # with open('D:\projects\\features','r',encoding='utf-8') as dir :
    #     print(dir.readlines())
    
    # for ele in name_list:
    #     print(ele)
    
    dir_file_list = os.listdir('E:\Project\python\py_study\source_file')
    print(dir_file_list)
    
    with open('E:\Project\python\py_study\source_file\\tmp.txt','r',encoding='utf-8') as create_file_name_list:
        for name in create_file_name_list:
            if name not in dir_file_list:
                os.mkdir()

if __name__ == '__main__':
    main()