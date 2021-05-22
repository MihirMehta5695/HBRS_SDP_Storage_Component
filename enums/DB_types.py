from enum import Enum


class DatabaseTypes(Enum):
    FLATFILE = "FLATFILES"
    SQL = "SQL"
    NOSQL = 'NOSQL'
