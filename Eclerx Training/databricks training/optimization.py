# Databricks notebook source
# MAGIC %sql
# MAGIC create table demo (id int, name varchar(100));
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into demo values(1,'Kairav');
# MAGIC insert into demo values(2,'Raj');
# MAGIC insert into demo values(3,'Kishan');
# MAGIC insert into demo values(4,'Sristi');
# MAGIC insert into demo values(5,'Abhi');
# MAGIC insert into demo values(6,'Ram');

# COMMAND ----------

# MAGIC %sql
# MAGIC desc detail demo

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from demo where id>4

# COMMAND ----------

# MAGIC %sql
# MAGIC optimize demo
# MAGIC zorder by (id)

# COMMAND ----------

# MAGIC %sql
# MAGIC desc detail demo

# COMMAND ----------

# MAGIC %md
# MAGIC Restore

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC desc history demo
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC restore table demo to version as of 6

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from demo

# COMMAND ----------

# MAGIC %sql
# MAGIC desc history demo

# COMMAND ----------

# MAGIC %sql
# MAGIC vacuum demo

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select * from demo version as of 4

# COMMAND ----------

# MAGIC %sql
# MAGIC vacuum demo retain 0 hours 

# COMMAND ----------

# MAGIC %sql
# MAGIC SET spark.databricks.delta.retentionDurationCheck.enabled = false

# COMMAND ----------

# MAGIC %sql
# MAGIC vacuum demo retain 0 hours 

# COMMAND ----------

# MAGIC %sql
# MAGIC create table demo_vendors (id int, name string) location '/FileStore/eclerx_metadata/vendors'

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into demo_vendors values (4,'Komal')

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table demo_vendors

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table demo

# COMMAND ----------


