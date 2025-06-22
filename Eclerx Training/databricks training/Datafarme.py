# Databricks notebook source
spark

# COMMAND ----------

user_data=([(1,'Naval'),(2,'Karan')])
user_schema="id int, name string"

df=spark.createDataFrame(data=user_data, schema=user_schema)

# COMMAND ----------

df.display()

# COMMAND ----------

df.show()

# COMMAND ----------

df.select("*")

# COMMAND ----------

df.select("*").display()

# COMMAND ----------

from pyspark.sql.functions import col

df1= df.select(col("id").alias("emp_id"))

# COMMAND ----------

df1.display()

# COMMAND ----------

df.withColumnRenamed("id","emp_id")

# COMMAND ----------

df.withColumnRenamed("id","emp_id").display()

# COMMAND ----------

df.withColumnsRenamed("id" : "emp_id","").display()
