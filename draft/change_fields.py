#author:shapemind
#dt: 2022/1/25 8:57
import re
"""
注意点：
1.后替换的字段，是否会覆盖掉之前的-换后字段中含有下面要替换的字段
2.怎样分词
"""
def main():
	fql_list = []
	field_compare_list = []
	field_needchange_list = []
	field_dict = {}
	new_fql_text = []
	# 得到fql文本
	with open('E:\\Nutstore_file\\我的坚果云\\WorkFile\\招行项目\\人行特征转移\\script_fql\\zs_debt.fql', 'r', encoding='utf-8') as fql:
		for line in fql:
			fql_list.append(line)
			
	with open('E:\\Nutstore_file\\我的坚果云\\WorkFile\\招行项目\\人行特征转移\\script_fql\\zs_debt.txt', 'rt', encoding='utf-8', newline='') as field_compare:
		lines = field_compare.readlines()
	# 去除不合规格式
	for line in lines:
		field_compare_list.append(line.rstrip())
	
	# 去除不必要替换的字段，得到最终需要替换的字段
	for field in field_compare_list:
		if (field[len(field) - 1] != '-'):
			field_list = field.split(' ')
			field_dict['%s'%field_list[1]] = field_list[0]
			field_needchange_list.append(field_list[1])
			field_list.clear()
	print(field_needchange_list)
	# 替换开始
	for line in fql_list:
		for old_field in field_needchange_list:
			field_index = line.find(old_field)
			after_old_field_index = field_index + len(old_field)
			before_old_field_index = field_index - 1

			if before_old_field_index < 0:
				before_old_field_index = -9999

			if before_old_field_index == -9999:
				before_letter = '('
			else:
				before_letter = line[before_old_field_index]

			try:
				after_letter = line[after_old_field_index]
			except IndexError:
				after_old_field_index = 9999
				after_letter = ')'
			if (re.match(r'[a-zA-Z_]', before_letter)) is None and (re.match(r'[a-zA-Z_]', after_letter)) is None:
				new_fql = line.replace(old_field, field_dict[old_field])
				new_fql_text.append(new_fql)

	with open('zs_debt_new.fql','w',encoding='utf-8') as new_fql:
		for line in new_fql_text:
			new_fql.write(line)

	

	
if __name__ == '__main__':
    main()