import json

from db.DBUtils import DBUtils


def get_input():
    return 'sqlite'


if __name__ == '__main__':
    input_name = get_input()
    with open('properties.json') as json_file:
        config_data = json.load(json_file)
    # print(config_data)
    db_utils = DBUtils()
    db_connection_details = r'pythonsqlite.db'
    # db_utils.connect_sqlite(r"./pythonsqlite.db")
    # print(config_data[input_name])
    db_utils.connect(config_data[input_name])
