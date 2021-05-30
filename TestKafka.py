from kafka import KafkaConsumer, KafkaProducer


class MyKafkaCons():
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')

    def run(self):
        future = self.producer.send('foobar', b'pointcloud <3')
        print('done')


if __name__ == '__main__':
    cons = MyKafkaCons()
    cons.run()
