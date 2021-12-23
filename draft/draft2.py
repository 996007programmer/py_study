

def main():
    res_data = []
    with open('res.txt','r',encoding='utf-8') as res:
        for line in res:
            res_data.append(line.replace('\n','').replace(',',''))
    print(res_data)

if __name__ == '__main__':
    main()