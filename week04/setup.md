```make conda-update
make conda-update
conda activate utec-bigdata-2022-1
make pip-tools
```

* Spark with docker:

```shell
docker run -it --rm --user root -p 8888:8888 -e NB_UID="$(id -u)" -e NB_GID="$(id -g)" -v /home/username/Documents/utec/bigdata/utec-bigdata-2022-1:/home/jovyan/work jupyter/pyspark-notebook
```

* Spark without docker

Add these paths to your bash file with  `nano ~/.bashrc`

```shell
export SPARK_HOME=/your_path_where_your_downloaded_spark/bigdata/spark-3.2.1-bin-hadoop3.2
export PATH=$PATH:$SPARK_HOME/bin
export PATH=$PATH:~/anaconda3/bin
export PYTHONPATH=${SPARK_HOME}/python/:$(echo ${SPARK_HOME}/python/lib/py4j-*-src.zip):${PYTHONPATH}
export PYSPARK_DRIVER_PYTHON="jupyter"
export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
export PYSPARK_PYTHON=python3
export PATH=$PATH:$JAVA_HOME/jre/bin
```
