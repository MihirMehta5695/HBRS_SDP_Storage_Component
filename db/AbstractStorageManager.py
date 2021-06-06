from abc import ABC, abstractmethod


class AbstractStorageManager(ABC):

    @abstractmethod
    def create_query(self, conn, query):
        pass

    @abstractmethod
    def read_query(self, conn, query):
        pass

    @abstractmethod
    def update_query(self, conn, query):
        pass

    @abstractmethod
    def delete_query(self, conn, query):
        pass

    @abstractmethod
    def list_query(self, conn, query):
        pass

    @abstractmethod
    def create_table(self, conn, query):
        pass

    @abstractmethod
    def delete_table(self, conn, query):
        pass
