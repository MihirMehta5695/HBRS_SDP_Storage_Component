import json

from db import DB_Manager
from helper import convert_message
from kafka import KafkaConsumer

# Constant to connect to kafka topic
topic_name = "hsrb_monitoring_rgbd"

event_listener = KafkaConsumer(
    'hsrb_monitoring_rgbd', value_deserializer=lambda m: json.loads(m.decode('utf-8')))

if __name__ == '__main__':

    with open('properties.json') as json_file:
        config_data = json.load(json_file)

    if config_data['enable_storage']:
        for message in event_listener:
            event_log = convert_message(message)
            print(event_log)
