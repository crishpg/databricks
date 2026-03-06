# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM `workspace`.`default`.`global_superstore`;

# COMMAND ----------

display(_sqldf)

# COMMAND ----------

filtered_df = _sqldf.filter(_sqldf.FirstName == 'Mike')



# COMMAND ----------

display(filtered_df)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SHOW TABLEs

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY workspace.default.global_superstore

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE DETAIL workspace.default.global_superstore

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DELETE FROM workspace.default.global_superstore WHERE OrderDate < '2011-02-01'

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY workspace.default.global_superstore

# COMMAND ----------


