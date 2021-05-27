from ecommerce.config.config import ConfigReader
from pymongo import MongoClient


class DBConnection:
    def __init__(self):
        try:
            # Load config settings
            config = ConfigReader()
            self.config = config.get_config()
            return self.__connect()
        except Exception as e:
            print('Error: ',e)
            raise Exception(e)

    def __connect(self):
        try:
            if self.config['DEFAULT']['ENV'] == 'local':
                db = MongoClient(f"mongodb+srv://{self.config['LOCAL']['MONGO_USERNAME']}:{self.config['LOCAL']['MONGO_PASSWORD']}@{self.config['LOCAL']['MONGO_CLUSTER']}/{self.config['LOCAL']['DB_NAME']}?retryWrites=true&w=majority")
            else:
                db = MongoClient(f"mongodb+srv://{self.config['PROD']['MONGO_USERNAME']}:{self.config['PROD']['MONGO_PASSWORD']}@{self.config['LOCAL']['MONGO_CLUSTER']}/{self.config['PROD']['DB_NAME']}?retryWrites=true&w=majority")
            return db
        except Exception as e:
            raise Exception('Error: ', e)