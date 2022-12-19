from pyspark import SparkSession
from pyspark.conf import SparkConf
from pyspark.sql import Row,Column
from pyspark.sql.functions import *
from pyspark.sql.types import *

conf.setMaster("local")
spark=SparkSession.builder.config(conf=SparkConf())

data_source=PATH_IN_S3

df=spark.read.option('header',True).option('inferSchema',True).csv(data_source)
df.show(3,truncate=False)

def execute_rules():
  import lob_child as lob
  lob.lob_rule()
 
if __name__=='__main__':
  execute_rules()
