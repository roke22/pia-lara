from pialara.db import db


class MongoModel:
    collection_name = None

    def __init__(self):
        self.db = db

    def find(self, params=None):
        return self.db[self.collection_name].find(params)

    def update_one(self, mongo_filter, new_values, upsert=False):
        return self.db[self.collection_name].update_one(mongo_filter, new_values, upsert=upsert)

    def update_many(self, mongo_filter, new_values, upsert=False):
        return self.db[self.collection_name].update_many(mongo_filter, new_values, upsert=upsert)

    def insert_one(self, values):
        return self.db[self.collection_name].insert_one(values)

    def insert_many(self, values):
        return self.db[self.collection_name].insert_many(values)
