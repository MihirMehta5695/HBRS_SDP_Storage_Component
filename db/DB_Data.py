from enums import Log_Level


class DB_Data():
    def __init__(self, source, time_stamp, log_level: Log_Level):
        self.source = source
        self.time_stamp = time_stamp
        self.log_level = log_level
