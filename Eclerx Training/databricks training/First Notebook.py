# Databricks notebook source
dbutils.fs.help()

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

print("hello")

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS my_db

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

# MAGIC %fs ls dbfs:/FileStore/

# COMMAND ----------

# MAGIC %sql
# MAGIC USE my_db;
# MAGIC CREATE TABLE my_db.my_student_tbl(Id varchar(100), Name varchar(100), Add varchar(100), Phone varchar(10));

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into my_db.my_student_tbl values(104,"Roshan", "Jaipur",'9838937740'),(103,"Kalyan", "Kokan",'9838937413')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from my_db.my_student_tbl

# COMMAND ----------

# MAGIC %sql
# MAGIC update my_db.my_student_tbl set Id=102 where Name='Asha';

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from my_db.my_student_tbl

# COMMAND ----------








