def main():
	field_dict = {
		'AAA' : '-',
		'bbb' : 'BB',
		'CCC' : 'CC'
	}
	
	final_dict = {key: value for key, value in field_dict.items() if value != '-'}
	final_list = {key for key in field_dict}
	print(final_list)
	print(final_dict)
if __name__ == '__main__':
    main()