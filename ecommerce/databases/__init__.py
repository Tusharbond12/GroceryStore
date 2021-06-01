from ecommerce.config.logger import AppLogger
from pymongo import MongoClient
import os

class DBConnection(AppLogger):
    def __init__(self):
        super(DBConnection, self).__init__()
        self.db = self.__connect()

    def __connect(self):
        try:
            if self.config['DEFAULT']['ENV'] == 'local':
                db = MongoClient(f"mongodb+srv://{self.config['LOCAL']['MONGO_USERNAME']}:{self.config['LOCAL']['MONGO_PASSWORD']}@{self.config['LOCAL']['MONGO_CLUSTER']}/{self.config['LOCAL']['DB_NAME']}?retryWrites=true&w=majority")
            else:
                db = MongoClient(f"mongodb+srv://{self.config['PROD']['MONGO_USERNAME']}:{self.config['PROD']['MONGO_PASSWORD']}@{self.config['LOCAL']['MONGO_CLUSTER']}/{self.config['PROD']['DB_NAME']}?retryWrites=true&w=majority")
            return db[self.config['PROD']['DB_NAME']]
        except Exception as e:
            self.log('Error: ' + str(e) + ' on file: '+ os.path.dirname(os.path.realpath(__file__))
                     )