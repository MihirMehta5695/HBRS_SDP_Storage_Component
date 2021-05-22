import json

from db_utils.DBUtils import DBUtils


def get_input():
    return 'sqlite'


if __name__ == '__main__':
    input_name = get_input()
    with open('properties.json') as json_file:
        config_data = json.load(json_file)
    print()
    db_utils = DBUtils()
    db_connection_details = r'pythonsqlite.db'
    # db_utils.connect_sqlite(r"./pythonsqlite.db")
    db_utils.connect(config_data[input_name])
