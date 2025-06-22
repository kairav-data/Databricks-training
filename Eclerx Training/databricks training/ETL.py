# Databricks notebook source
# MAGIC
# MAGIC %sql
# MAGIC
# MAGIC create database if not exists formula1

# COMMAND ----------

# DBTITLE 1,ETL
from pyspark.sql.functions import *

# Extract
csv_path="dbfs:/FileStore/Training_files/circuits.csv"
df=spark.read.csv(csv_path,header=True,inferSchema =True)

# Transform
df_final =df.withColumnsRenamed({"circuitId":"circuit_id","circuitref":"circuit_ref"})\
            .withColumn("current_Date",current_date())\
            .drop("url")

# Load
df_final.write.mode("overwrite").saveAsTable("formula1.tbl_circuit")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from formula1.tbl_circuit

# COMMAND ----------

df_final.write.mode("overwrite").format("parquet").saveAsTable("formula1.tbl_circuit_parquet")

# COMMAND ----------

# MAGIC %sql
# MAGIC desc extended hive_metastore.formula1.tbl_circuit

# COMMAND ----------

# MAGIC %sql
# MAGIC desc extended hive_metastore.formula1.tbl_circuit_parquet
