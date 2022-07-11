import requests
import json
import sys
import codecs
import csv
import pandas as pd

domains = sys.argv[0]
src_path = '/mdx/data/t_table_0623/kx_udf_t_{}_testData.json'.format(domains)
save_path = '/mdx/csv/{}.csv'.format(domains)
res_list = []

def xfeval(data):
	return res

with open(src_path) as f:
	
	for line in f:
		full_json = json.loads(line)
		data_json = full_json['kx_udf_t_{}_testData'.format(domains)]
		res = data_json.T.apply(lambda data : xfeval(data))
		res_list.append(res)

with open(save_path,'w',encoding='utf-8') as f:
	for ele in res_list:
		f.write(ele+'\n')