import pymongo
from pymongo import MongoClient
import sys
from flask import current_app

# db = current_app.db
class SettingUpDB:
    def __init__(self, query, coll_name):
        self.query = query
        self.coll_name = coll_name

    def construct_db(self):
        self.coll = db[self.coll_name]
        return self.coll

    def inserts_to_db(self, db, coll, query):
        self.post_id = coll.insert(self.query, check_keys=False)
        print(f"Data inserted for object ID:: {self.post_id}")

    def updates_info(self, db, coll, query, new_val):
        self.query = query
        self.new_val = new_val
        self.updatedColl = coll.update_many(self.query, self.new_val)

    def fetch_info(self, db, coll, query):
        self.results = coll.find(query)
        return self.results

    def aggregate_query(self, db, coll, query_in_list):
        self.results = coll.aggregate(query_in_list)
        return self.results


def insert_data(query, collection):
    c_db = SettingUpDB(query, collection)
    coll = c_db.construct_db()
    c_db.inserts_to_db(db, coll, query)


def fetch_data(collection, query):
    c_db = SettingUpDB(query, collection)
    coll = c_db.construct_db()
    res = c_db.fetch_info(db, coll, query)
    return res


def grouping_data(collection, query):
    c_db = SettingUpDB(query, collection)
    coll = c_db.construct_db()
    res = c_db.aggregate_query(db, coll, query)
    return res


def updating_data(query, new_val, collection):
    c_db = SettingUpDB(query, collection)
    coll = c_db.construct_db()
    c_db.updates_info(db, coll, query)