import json
from signal import SIGINT, signal

import yaml

from db.Storage_Manager import SQLManager, create_manager
from helper import convert_message
from kafka import KafkaConsumer
from settings import init

# from db import DB_Manager

# Constant to connect to kafka topic
topic_name = "hsrb_monitoring_rgbd"

# Kakfa topic listener
event_listener = KafkaConsumer(
    'hsrb_monitoring_rgbd', value_deserializer=lambda m: json.loads(m.decode('utf-8')))


def exit_handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully! Cheers :D')
    exit(0)


if __name__ == '__main__':

    # Reference Link:
    # https://www.devdungeon.com/content/python-catch-sigint-ctrl-c
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, exit_handler)

    # use yaml
    with open('properties.yaml') as json_file:
        config_data = yaml.load(json_file)

    if config_data['enable_storage']:

        db_name = config_data['config']['storage_name']
        db_config = config_data['available_storages'][db_name]
        init(db_config)
        storage_manager = create_manager(db_config)
        for message in event_listener:
            event_log = convert_message(message, db_config['type'])
            storage_manager.create_query(event_log)
