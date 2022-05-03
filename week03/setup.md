Docker images with spark

1. p7hb/docker-spark

```

docker run -it -p 4040:4040 -p 8080:8080 -p 8081:8081 -h spark --name=spark p7hb/docker-spark
```

`docker rm -v spark`

2. Explore in docker hub

type pyspark (https://hub.docker.com/r/jupyter/pyspark-notebook)

`docker pull jupyter/pyspark-notebook`

`docker run -it --rm -p 10000:8888 -h spark --name=spark jupyter/pyspark-notebook`

3. download csv

   `wget https://raw.githubusercontent.com/GovLab/OpenData500/master/static/files/us/us_companies.csv`
4. spark - scala

docker start 43b2ab5c8f8e

docker exec -i -t 43b2ab5c8f8e /bin/bash

spark-shell --total-executor-cores 2 --executor-memory 4g

spark-shell --total-executor-cores 2 --executor-memory 4g

val companies = spark.read.format("com.databricks.spark.csv").option("header","true").option("delimiter",",").load("/home/csv/us_companies.csv").na.fill("")

companies.printSchema

companies.write.parquet("/home/parquetFile/companies.parquet")

du -h companies.parquet  -> 300k

jupyter-notebook

docker start 43b2ab5c8f8e

1.-   docker exec -i -t  -p 10000:8888 43b2ab5c8f8e /bin/bash

2.-   docker run -it --rm -p 10000:8888 -h spark --name=spark jupyter/pyspark-notebook

**

The** **difference between “docker run” and “docker exec” is that “docker exec” executes a command on a running container. On the other hand, “docker run” creates a temporary container, executes the command in it and stops the container when it is done.**

docker ps -a

docker start id_c

docker run -it -p 10000:8888 jupyter/pyspark-notebook

docker run -it --rm  -p 10000:8888  -v /Users/richard:/home/jovyan/work jupyter/pyspark-notebook  /bin/bash

docker run -it --rm  -p 8888:8888  -v /Users/richard:/home/jovyan/work jupyter/pyspark-notebook

docker run -d -v /Users/richard:/home/jovyan/work -p 8888:8888 --user root -e CHOWN_EXTRA="/home/jovyan/work" -e CHOWN_EXTRA_OPTS="-R" jupyter/pyspark-notebook

final

docker run -it --rm
--user root
-p 8888:8888
-e NB_UID="$(id -u)"
-e NB_GID="$(id -g)"
-v /Users/richard:/home/jovyan/work
jupyter/pyspark-notebook

import pyspark
from pyspark import SparkContext
#lines = sc.textFile("README.md")§§
try:
sc=SparkContext()
except:
print("Context is already running")

nums= sc.parallelize([1,2,3,4])
nums.take(1)
squared = nums.map(lambda x: x*x).collect()
for num in squared:
print('%i ' % (num))

https://jupyter-docker-stacks.readthedocs.io/en/latest/using/troubleshooting.html

`docker run -it --rm --user root -p 8888:8888 -e NB_UID="$(id -u)" -e NB_GID="$(id -g)" -v /Users/richard:/home/jovyan/work jupyter/pyspark-notebook`

```
spark-shell -i file.scala
```
