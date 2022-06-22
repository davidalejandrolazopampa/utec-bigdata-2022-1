# pyspark --driver-class-path postgresql-9.4.1207.jar --jars postgresql-9.4.1207.jar sparkSqlJdbc.py

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext

conf = SparkConf().setMaster("local[3]").setAppName("Sparksql")
sc = SparkContext.getOrCreate(conf=conf)

sqlsc = SQLContext(sc)

# Note: JDBC loading and saving can be achieved via either the load/save or jdbc methods
# Loading data from a JDBC source
jdbcDF = sqlsc.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql:sparksql") \
    .option("dbtable", "schema.tablename") \
    .option("user", "username") \
    .option("password", "password") \
    .load()

jdbcDF2 = sqlsc.read \
    .jdbc("jdbc:postgresql:dbserver", "schema.tablename",
          properties={"user": "username", "password": "password"})

# Specifying dataframe column data types on read
jdbcDF3 = sqlsc.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql:dbserver") \
    .option("dbtable", "schema.tablename") \
    .option("user", "username") \
    .option("password", "password") \
    .option("customSchema", "id DECIMAL(38, 0), name STRING") \
    .load()

# Saving data to a JDBC source
jdbcDF.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql:dbserver") \
    .option("dbtable", "schema.tablename") \
    .option("user", "username") \
    .option("password", "password") \
    .save()

jdbcDF2.write \
    .jdbc("jdbc:postgresql:dbserver", "schema.tablename",
          properties={"user": "username", "password": "password"})

# Specifying create table column data types on write
jdbcDF.write \
    .option("createTableColumnTypes", "name CHAR(64), comments VARCHAR(1024)") \
    .jdbc("jdbc:postgresql:dbserver", "schema.tablename",
          properties={"user": "username", "password": "password"})
