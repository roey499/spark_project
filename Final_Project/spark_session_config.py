#spark session config

from pyspark.sql import SparkSession

# ex 1+2+3+4 - Cars
#spark_cars = SparkSession.builder.master("local").appName('CarsGenerator').getOrCreate()

spark = SparkSession \
    .builder \
    .appName("DataEnrichment") \
    .master("local") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")\
    .config("spark.hadoop.fs.s3a.access.key", 'minioadmin')\
    .config("spark.hadoop.fs.s3a.secret.key", 'minioadmin')\
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000")\
    .config("spark.hadoop.fs.s3a.path.style.access", "true")\
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0') \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")\
    .getOrCreate()

