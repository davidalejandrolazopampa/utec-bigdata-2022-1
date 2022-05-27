

"""zookeper
    Apache kafka usa zookeper para almacenar metadatos del cluster de kafka y detalles de los consumidores
    vim config/zookeeper.properties
    ./zookeeper-server-start.sh ../config/zookeeper.properties

    cp server.properties server-1.properties
    cp server.properties server-2.properties
    vim server-1.properties
        broker.id=1
        listeners=PLAINTEXT 
    FACTOR DE REPLICACION - lista de nodos o brokers -> leader
    import data/csv/Solaris_min15_Almeria_Spain.csv  -> produce
    consume and send to redis - order and make forecasting
    sklearn prediction - forecasting

    slides -> factor de replicacion


    do the project format !!
"""
