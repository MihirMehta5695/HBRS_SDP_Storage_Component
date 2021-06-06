import json

# from db.DBUtils import DBUtils
from db import DB_Manager


def get_input():
    return {

        "monitorName": "rgbd_monitor",
        "monitorDescription": "Monitor verifying that the pointcloud of the RGBD camera has no NaNs",
        # "healthStatus": "healthy",
        "healthStatus":
            {
                "nans": True
            }
    }


# if __name__ == '__main__':
#     input_name = get_input()
#     with open('properties.json') as json_file:
#         config_data = json.load(json_file)
#     # print(config_data)
#     db_utils = DBUtils()
#     db_connection_details = r'pythonsqlite.db'
#     # db_utils.connect_sqlite(r"./pythonsqlite.db")
#     # print(config_data[input_name])
#     db_utils.connect(config_data[input_name])

if __name__ == '__main__':
    input_data = get_input()
    with open('properties.json') as json_file:
        config_data = json.load(json_file)

    if config_data['enable_storage']:
        print(f"Enabled Storage? : {config_data['enable_storage']}")
        db_manager = DB_Manager.DBManager()
        db_name = config_data['config']['storage_name']
        db_config = config_data['available_storages'][db_name]
        # print(f"[DB_MAIN] Selected DB Config : {db_config}")
        db_manager.create_connection(db_config)
