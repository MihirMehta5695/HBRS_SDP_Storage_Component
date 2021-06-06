import settings
from db.AbstractStorageManager import AbstractStorageManager


class SQLManager(AbstractStorageManager):
    def __init__(self):
        print("[SQLManager] Init Done")
        self.session = settings.Session()

    def create_query(self, conn, query):
        pass

    def create_query(self, data):
        print('[SQLManager] [create_query] Adding Object!')
        self.session.add(data)
        self.session.commit()

    def read_query(self, conn, query):
        pass

    def update_query(self, conn, query):
        pass

    def delete_query(self, conn, query):
        pass

    def list_query(self, conn, query):
        pass

    def create_table(self, conn, query):
        pass

    def delete_table(self, conn, query):
        pass

    def __del__(self):
        # body of destructor
        print("[Storage_Manager] Destroying Object")
