from ecommerce.databases.connection import DBConnection


class Model(DBConnection):
    def __init__(self, collection):
        self.db = super(Model, self).__init__()
        self.collection = self.db[collection]

    def create(self, data: dict):
        return self.collection.insert_one(data)

    def create_multiple(self, data: list):
        return self.collection.insert_many(data)

    def find(self, select: dict = {}):
        return self.collection.find({}, select)

    def query(self, query: dict = {}):
        return self.collection.find(query)

    def delete(self, query: dict = {}):
        return self.collection.delete_one(query)

    def delete_many(self, query: dict = {}):
        return self.collection.delete_many(query)