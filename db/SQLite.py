import sqlite3
from sqlite3 import Connection, Error


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_query(conn: Connection, project):

    cur = conn.cursor()
    cur.execute(queries)
    conn.commit()
    return cur.lastrowid
