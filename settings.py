from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def init(conn_details):
    print(f"[Settings1] Connection Details : {conn_details}")
    if conn_details["type"] == "SQL":
        init_sql(conn_details)


def init_sql(conn_details):

    # Reference Link:
    # https://stackoverflow.com/q/63368099
    global engine, Session
    engine = create_engine(conn_details['connection_string'])
    Session = sessionmaker(bind=engine)
    print("[Settings1] Init Session", Session)
