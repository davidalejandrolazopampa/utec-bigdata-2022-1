
from confluent_kafka import Producer, TopicPartition
import socket


class App():
    def __init__(self):
        self.topic = 'bigdata-streams'
        self.conf_producer = {
            'bootstrap.servers': 'localhost:9092',
            'client.id': socket.gethostname(),
            # 'enable.idempotence': True,
        }
        self.producer = Producer(self.conf_producer)

    def produce(self, data):
        #self.producer.produce(self.topic, data)
        self.producer.produce(self.topic, key=None, value=data)
        self.producer.flush()


app = App()
app.produce("utec2022-1")
