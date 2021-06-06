import sqlite3
from sqlite3 import Error

from enums.DB_types import DatabaseTypes


class DBUtils:

    def __init__(self):
        super()
        self.connections = {}

    def connect(self, config):
        # print(f"Here in DB Utils: {config}")
        configs = {str(DatabaseTypes.SQL): self._connect_sql_alchemy,
                   str(DatabaseTypes.FLATFILE): self._connect_flatfiles,
                   str(DatabaseTypes.NOSQL): self._connect_sqlite,
                   str(DatabaseTypes.SQLite): self._connect_sqlite}
        configs[str(DatabaseTypes.SQLite)](config)

    def _connect_sql_alchemy():
        pass

    def _connect_kafka():
        pass

    def _connect_flatfiles():
        pass

    def _connect_sqlite(self, db_config):
        print(self, db_config)
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_config["file_name"])
            if conn:
                self.connections[str(DatabaseTypes.SQLite)] = conn
        except Error as e:
            print(e)
