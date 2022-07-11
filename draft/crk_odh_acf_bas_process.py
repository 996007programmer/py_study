#author:shapemind
#dt: 2022/6/14 14:24

# coding: utf-8# 行外非人行-逾期历史
import pandas as pd
import imp
import time
import base64
import json
import glob
import yaml
from pathlib import Path
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql import functions as F
from source import primaryKey, db, prefix
def get_fields(inputSchema_map, subdomain):
	inputSchema = inputSchema_map.get(subdomain)
	fields = [i['name'] for i in inputSchema if i.get("required")]
	print('required fields...', fields)
	return fields
def run(spark, subdomain, inputSchema_map, prt_dt):
	print("""-------{} process ---------""".format(subdomain))
	fields = get_fields(inputSchema_map, subdomain)
	query1_fields = list("t1." + item for item in fields)
	t1 = """select
			t1.id_no as cert_no,
			{4},
			dense_rank() over (partition by t1.id_no order by t1.rpt_tim desc) as rn
			from {0}.{1}nls09_zx11600a t1
			where t1.prt_dt='{2}'""".format(db, prefix, prt_dt, ",".join(query1_fields))
	t1_df = spark.sql(t1)
	fir_tbl = 'fir_tbl'
	t1_df.createOrReplaceTempView(fir_tbl)
	sql2 = """ select * from {} where rn = 1 """.format(fir_tbl)
	fin_df = spark.sql(sql2)
	return fin_df