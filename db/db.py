from pymongo import MongoClient


class Database:

    def __init__(self,connection_string) -> None:
        self.connection_string = connection_string

    def GetClient(self):
        client = MongoClient(self.connection_string)
        return client
    

