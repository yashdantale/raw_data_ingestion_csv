# 🧊 Raw Data Ingestion – CSV to Iceberg

This repo demonstrates how to ingest a raw CSV file into a simulated Iceberg table using PySpark. 

## 🔧 Steps

1. Read `products.csv`
2. Ingest it as the raw layer (`raw_db.products`)
3. Simulated Iceberg format using partitioned CSV (can plug into Iceberg with catalog support)

## 📂 Files
- `scripts/ingest_raw.py`: Raw ingestion logic
- `sql/create_raw.sql`: Iceberg table DDL
