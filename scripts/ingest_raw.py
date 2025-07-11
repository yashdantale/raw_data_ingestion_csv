from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RawIngestion") \
    .getOrCreate()

# Load raw CSV
df_raw = spark.read.csv("data/products.csv", header=True, inferSchema=True)

# Write to raw layer (simulate Iceberg as CSV)
df_raw.write.mode("overwrite").option("header", True).csv("iceberg_tables/raw")

print("✅ Raw data written to 'iceberg_tables/raw'")
