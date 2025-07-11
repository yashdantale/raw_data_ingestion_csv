-- Create RAW Layer Table
CREATE TABLE raw_db.products (
    Index BIGINT,
    Name STRING,
    Description STRING,
    Brand STRING,
    Category STRING,
    Price DOUBLE,
    Currency STRING,
    Stock BIGINT,
    EAN STRING,
    Color STRING,
    Size STRING,
    Availability STRING,
    `Internal ID` BIGINT
)
USING ICEBERG
TBLPROPERTIES (
  'format-version'='2',
  'write.format.default'='parquet'
);
