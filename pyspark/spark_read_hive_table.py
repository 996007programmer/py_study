#author:shapemind
#dt: 2022/3/11 8:05
from pyspark.sql import SparkSession
if __name__ == '__main__':
	spark_task = SparkSession.Builder()\
		.appName('read_hive_table')\
		.master('local')\
		.enableHiveSupport()\
		.getOrCreate()