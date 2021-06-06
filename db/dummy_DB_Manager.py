import json
from datetime import datetime

from db.SQLite import SqlLite
from enums.DB_types import DatabaseTypes


class DBManager():
    def __init__(self):
        super()
        # self.connections = {}
        # self.config_types = {
        #     str(DatabaseTypes.SQL): self._connect_sql_alchemy,
        #     str(DatabaseTypes.FLATFILE): self._connect_flatfiles,
        #     str(DatabaseTypes.NOSQL): self._connect_sqlite,
        #     str(DatabaseTypes.SQLite): self._connect_sqlite
        # }
        # print("[DBManager] [__init__] Initialized!")

    def create_connection(self, config):
        print(f"[DBManager] [create_connection] Got config: {config}")
        sql_lite = SqlLite()
        conn = sql_lite.connect(config)
        sql_query = f"""
        INSERT INTO EVENTLOG
        (
            TIMESTAMP,
            MONITOR_NAME,
            HEALTH_STATUS
        )
        values
        (
            {int(datetime.now().timestamp())},
            'rgbd_monitor',
            '{json.dumps({"healthStatus":{"nans": True}})}'
        );
        """
        resp = sql_lite.insert_query(conn, sql_query)
        print(f"[DBManager] [create_connection] Insert into DB response: {resp}")

    def _connection_exists(self, config):
        pass
