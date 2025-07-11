from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RawIngestion") \
    .getOrCreate()

# Load raw CSV
df_raw = spark.read.csv("data/products.csv", header=True, inferSchema=True)

# Write to raw layer table
df_raw.write.format("iceberg").mode("overwrite").insertInto("raw_db.products")

print("✅ Raw data written to raw_db.products")
