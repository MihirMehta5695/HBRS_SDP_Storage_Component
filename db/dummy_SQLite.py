import sqlite3
from sqlite3 import Connection, Error


class SqlLite:

    def __init__(self):
        super()

    def connect(self, config):
        """ create a database connection to the SQLite database
            specified by db_file
        :param config: database config file
        :return: Connection object or None
        """
        print(f"[SQLite] [connect] config: {config}")
        conn = None
        try:
            conn = sqlite3.connect(config['file_name'])
        except Error as e:
            print(e)

        return conn

    def create_table(self, conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        sql = """CREATE TABLE IF NOT EXISTS EVENTLOG(TIMESTAMP VARCHAR2(50) PRIMARY KEY, MONITOR_NAME VARCHAR2(50),HEALTH_STATUS INTEGER, ADDITIONAL_DATA VARCHAR2(100));"""
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def insert_query(self, conn: Connection, sql_query):

        cur = conn.cursor()
        cur.execute(sql_query)
        conn.commit()
        return cur.lastrowid

    def read_query(self, conn: Connection, sql_query):
        cur = conn.cursor()
        cur.execute(sql_query)
        rows = cur.fetchall()
        return rows
