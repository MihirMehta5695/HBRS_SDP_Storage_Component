import time
import unittest
from datetime import datetime
from signal import SIGINT, signal

import yaml

from db.Storage_Manager import SQLManager, create_manager
from helper import convert_message, create_eventlog
from settings import init


class MongoTester(unittest.TestCase):

    @classmethod
    def setUpClass(MongoTester):
        with open('properties.yaml') as config_file:
            MongoTester.config_data = yaml.safe_load(config_file)

        if MongoTester.config_data['enable_storage']:
            MongoTester.db_name = MongoTester.config_data['config']['storage_name']
            MongoTester.db_config = MongoTester.config_data['available_storages'][MongoTester.db_name]
            init(MongoTester.db_config)
            # sql_mgr = SQLManager()
            MongoTester.storage_manager = create_manager(MongoTester.db_config)

    @classmethod
    def tearDownClass(MongoTester):
        # print("[MongoTest]-[tearDownClass] Tearing down...!")
        print()

    def test_insert(self):
        message = {'timestamp': f'{time.time()}', "value": {'monitorName': "rgbd_monitor",
                                                            "healthStatus": {"nans": True}}}
        event_log = create_eventlog(message, self.db_config['type'])
        result = self.storage_manager.create_query(event_log)
        print(f"[MongoTest]-[test_insert] result : {result} ")
        self.assertTrue(result)

    def test_read(self):
        message = {'timestamp': str(1624176474.522729), "value": {'monitorName': "rgbd_monitor",
                                                                  "healthStatus": {"nans": True}}}
        event_log = create_eventlog(message, self.db_config['type'])
        result = self.storage_manager.read_query(event_log)
        print(f"[MongoTest]-[test_read] result : {result} ")
        self.assertTrue(result)

    def test_update(self):
        message = {'timestamp': str(1624173972.3457322), "value": {'monitorName': "rgbd_monitor",
                                                                   "healthStatus": {"nans": True}}}
        event_log = create_eventlog(message, self.db_config['type'])
        result = self.storage_manager.update_query(event_log)
        print(f"[MongoTest]-[test_update] result : {result} ")
        self.assertTrue(result)

    def test_delete(self):
        message = {'timestamp': str(1624174052.8045669), "value": {'monitorName': "rgbd_monitor",
                                                                   "healthStatus": {"nans": True}}}
        event_log = create_eventlog(message, self.db_config['type'])
        result = self.storage_manager.delete_query(event_log)
        print(f"[MongoTest]-[test_delete] result : {result} ")
        self.assertTrue(result)

    def test_list(self):
        result = self.storage_manager.list_query()
        print(f"[MongoTest]-[test_list] result : {result} ")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
