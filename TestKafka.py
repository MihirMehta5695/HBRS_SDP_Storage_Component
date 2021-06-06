import json

from kafka import KafkaConsumer, KafkaProducer


class MyKafkaCons():
    def __init__(self):
        # self.topic_name = 'hsrb_monitoring_rgbd'
        self.topic_name = 'hsrb_monitoring_rgbd'
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')
        # self.consumer = KafkaConsumer(bootstrap_servers='localhost:9092')

    def run(self):
        # future = self.producer.send('foobar', b'pointcloud <3')
        self.event_listener = KafkaConsumer(
            'hsrb_monitoring_rgbd', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        for message in self.event_listener:
            if message.value['healthStatus']['nans']:
                print(message.value)


if __name__ == '__main__':
    cons = MyKafkaCons()
    cons.run()
