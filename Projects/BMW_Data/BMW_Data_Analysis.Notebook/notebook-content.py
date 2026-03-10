# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "273a29fe-d236-4f0b-bb65-4c078b975984",
# META       "default_lakehouse_name": "BMW_LH",
# META       "default_lakehouse_workspace_id": "38aa245e-71f1-4f8d-97b7-a9438dd1334b",
# META       "known_lakehouses": [
# META         {
# META           "id": "273a29fe-d236-4f0b-bb65-4c078b975984"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM BMW_LH.BMW_data_bronze.bmw_data")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.cache()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = df.withColumn('TotalSales', col('Price_USD') * col('Sales_Volume'))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.format('delta').mode('overwrite').save('Tables/Bmw_Silver/BMW_Silver_Data')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
