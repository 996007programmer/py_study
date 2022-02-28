#author:shapemind
#dt: 2022/2/23 15:56

import re
def main():
	fql_result = []
	# 打开原fql结果
	with open('E:\Project\python\py_study\source_file\\fql_result.txt', 'r', encoding='utf-8') as fql:
		for line in fql:
			if (re.match(r'[{}]', line)):
				continue
			no_pre = re.sub(r'^"','',line.lstrip())
			no_post = re.sub(r'":.+','',no_pre)
		
			fql_result.append(no_post)
	fql_result.sort()
	with open('E:\Project\python\py_study\source_file\\fql_result_format.txt','w',encoding='utf-8') as new_fql:
		for line in fql_result:
			new_fql.write(line)
	print(fql_result)
if __name__ == '__main__':
    main()