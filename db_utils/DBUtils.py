import sqlite3
from sqlite3 import Error

from enums.DB_types import DatabaseTypes


class DBUtils:

    def __init__(self):
        super()

    def connect(self, config):
        configs = {DatabaseTypes.SQL: self._connect_sql_alchemy,
                   DatabaseTypes.FLATFILE: self._connect_flatfiles,
                   DatabaseTypes.SQLite: self._connect_sqlite}

    def _connect_sql_alchemy():
        pass

    def _connect_kafka():
        pass

    def _connect_flatfiles():
        pass

    def _connect_sqlite(self, db_config):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_config.file_name)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
