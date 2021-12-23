def main():
	# data1 = []
	# with open('C:\\Users\\Craiditx\\Desktop\\3612.json',encoding='utf-8') as fs1:
	# 	for line in fs1:
	# 		str_line = str(line)
	# 		newstr_line = str_line.replace('\n','')
	# 		data1.append(newstr_line)
	#
	# data2 = []
	# with open('C:\\Users\\Craiditx\\Desktop\\minmax.json', encoding='utf-8') as fs2:
	# 	for line in fs2:
	# 		str_line = str(line)
	# 		newstr_line = str_line.replace('\n', '')
	# 		data2.append(newstr_line)
	#
	# print(data2)
	#
	# data3 = []
	# for i in range(len(data1)):
	# 	for j in range(len(data2)):
	# 		data3.append(data2[j] + data1[i] + '),')
	#
	# print(data3,sep='\n')
	#
	# with open('res.txt','w',encoding='utf-8') as wf:
	# 	for ele in data3:
	# 		wf.write(ele + '\n')
	
	# data1 = []
	# with open('C:\\Users\\Craiditx\\Desktop\\c3c4.json', encoding='utf-8') as fs1:
	# 	for line in fs1:
	# 		str_line = str(line)
	# 		newstr_line = str_line.replace('\n', '')
	# 		data1.append(newstr_line)
	# # print(data1)
	# data2 = []
	# with open('C:\\Users\\Craiditx\\Desktop\\minmax.json', encoding='utf-8') as fs2:
	# 	for line in fs2:
	# 		str_line = str(line)
	# 		newstr_line = str_line.replace('\n', '')
	# 		data2.append(newstr_line)
	#
	# # print(data2)
	# #
	# data3 = []
	# for i in range(len(data1)):
	# 	for j in range(len(data2)):
	# 		data3.append(data2[j] + data1[i] + '),')
	#
	# print(data3)
	#
	# with open('res2.txt', 'w', encoding='utf-8') as wf:
	# 	for ele in data3:
	# 		wf.write(ele + '\n')
	
	data1 = []
	with open('C:\\Users\\Craiditx\\Desktop\\unitc3c4.json', encoding='utf-8') as fs1:
		for line in fs1:
			str_line = str(line)
			newstr_line = str_line.replace('\n', '')
			data1.append(newstr_line)
	print(data1)
	# data2 = []
	# with open('C:\\Users\\Craiditx\\Desktop\\minmax.json', encoding='utf-8') as fs2:
	# 	for line in fs2:
	# 		str_line = str(line)
	# 		newstr_line = str_line.replace('\n', '')
	# 		data2.append(newstr_line)
	#
	# # print(data2)
	# #
	data3 = []
	for i in range(len(data1)):
			data3.append('count_zero(' + data1[i] + ') as ' + data1[i] + '_Count,')

	print(data3)

	with open('res3.txt', 'w', encoding='utf-8') as wf:
		for ele in data3:
			wf.write(ele + '\n')
if __name__ == '__main__':
    main()