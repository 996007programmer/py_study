from pyspark.sql import SparkSession
import sys

def main():
	spark = SparkSession\
		.builder\
		.appName("wordcount")\
		.getOrCreate()
	
	inputPath = sys.argv[1]
	print('inputPath: {}'.format(inputPath))


if __name__ == '__main__':
    main()