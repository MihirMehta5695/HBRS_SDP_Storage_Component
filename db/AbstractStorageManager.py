from abc import ABC, abstractmethod


class AbstractStorageManager(ABC):

    @abstractmethod
    def create_query(self, data):
        pass

    @abstractmethod
    def read_query(self, query):
        pass

    @abstractmethod
    def update_query(self, query):
        pass

    @abstractmethod
    def delete_query(self, query):
        pass

    @abstractmethod
    def list_query(self, query):
        pass

    @abstractmethod
    def create_table(self, query):
        pass

    @abstractmethod
    def delete_table(self, query):
        pass
