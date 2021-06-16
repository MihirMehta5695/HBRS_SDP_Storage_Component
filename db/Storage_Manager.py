import settings
from db.AbstractStorageManager import AbstractStorageManager


def create_manager(db_config):
    # print(f"[Storage_Manager] dbConfig: {db_config}")
    db_type = db_config['type']
    if db_type == 'SQL':
        return SQLManager()
    if db_type == 'NOSQL' and db_config['name'] == 'mongodb':

        return MongoManager()


class SQLManager(AbstractStorageManager):
    def __init__(self):
        print("[SQLManager] Init Done")
        self.session = settings.Session()

    def create_query(self, data):
        print('[SQLManager] [create_query] Adding Object!')
        self.session.add(data)
        self.session.commit()

    def read_query(self,  query):
        pass

    def update_query(self, query):
        pass

    def delete_query(self, query):
        pass

    def list_query(self, query):
        pass

    def create_table(self, query):
        pass

    def delete_table(self, query):
        pass

    def __del__(self):
        # body of destructor
        print("[Storage_Manager] [SQLManger] Destroying Object")


class MongoManager(AbstractStorageManager):
    def __init__(self):
        print("[MongoManager] Init Done")
        self.session = settings.Session

    def create_query(self, data):
        print('[MongoManager] [create_query] Adding Object!')
        # print((type(data)))
        self.session.insert_one(data)
        # self.session.commit()

    def read_query(self,  query):
        pass

    def update_query(self, query):
        pass

    def delete_query(self, query):
        pass

    def list_query(self, query):
        pass

    def create_table(self, query):
        pass

    def delete_table(self, query):
        pass

    def __del__(self):
        # body of destructor
        print("[Storage_Manager] [MongoManager] Destroying Object")
