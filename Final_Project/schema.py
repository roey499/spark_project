from pyspark.sql import types as T

car_models_schema = T.StructType([
    T.StructField("model_id", T.IntegerType(), nullable=False),
    T.StructField("car_brand", T.StringType(), nullable=False),
    T.StructField("car_model", T.StringType(), nullable=False)
])

car_colors_schema = T.StructType([
    T.StructField("color_id", T.IntegerType(), nullable=False),
    T.StructField("color_name", T.StringType(), nullable=False)
])

sensor_data_schema = T.StructType([
    T.StructField("event_id", T.StringType(), True),
    T.StructField("event_time", T.StringType(), True),
    T.StructField("car_id", T.StringType(), True),
    T.StructField("speed", T.IntegerType(), True),
    T.StructField("rpm", T.IntegerType(), True),
    T.StructField("gear", T.IntegerType(), True)
])


samples_data_schema = T.StructType([
    T.StructField("event_id", T.StringType(), True),
    T.StructField("event_time", T.TimestampType(), True),
    T.StructField("car_id", T.StringType(), True),
    T.StructField("speed", T.IntegerType(), True),
    T.StructField("rpm", T.IntegerType(), True),
    T.StructField("gear", T.IntegerType(), True),
    T.StructField("expected_gear", T.DoubleType(), True),
    T.StructField("driver_id", T.StringType(), True),
    T.StructField("brand_name", T.StringType(), True),
    T.StructField("model_name", T.StringType(), True),
    T.StructField("color_name", T.StringType(), True)
])