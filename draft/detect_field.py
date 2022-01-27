#author:shapemind
#dt: 2022/1/27 10:19
import re
def main():
	field_list = []
	use_field_list = []
	with open('E:\Project\python\py_study\source_file\zs.txt','r',encoding='utf-8') as fields:
		for field in fields:
			field_list.append(field.strip())
			
	with open('E:\Project\python\py_study\source_file\zs.fql','r',encoding='utf-8') as fql:
		for line in fql:
			for field in field_list:
				if field_exist(field, line) and (field not in use_field_list):
					use_field_list.append(field)
	with open('E:\Project\python\py_study\source_file\\fql_field.txt','w',encoding='utf-8') as result:
		for field in use_field_list:
			result.write(field+'\n')
	print('done')

def field_exist(field :str, line: str) -> bool:
	tiny_field = field.strip()
	tiny_line = line.strip()
	
	field_index = tiny_line.find(tiny_field)
	if field_index == -1:
		return False
	after_old_field_index = field_index + len(tiny_field)
	before_old_field_index = field_index - 1
	
	if before_old_field_index < 0:
		before_old_field_index = -9999
		before_letter = '('
	else:
		before_letter = tiny_line[before_old_field_index]
	
	try:
		after_letter = tiny_line[after_old_field_index]
	except IndexError:
		after_old_field_index = 9999
		after_letter = ')'
	# 当且只有当被替换单词前后不是字母以及‘_’时，判断确实含有此字段
	if (re.match(r'[a-zA-Z_]', before_letter)) is None and (re.match(r'[a-zA-Z_]', after_letter)) is None:
		return True
	return False
if __name__ == '__main__':
    main()