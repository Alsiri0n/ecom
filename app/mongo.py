import pymongo
from pymongo import MongoClient
import sys
from flask import current_app
import json


def clear_data():
    current_app.db.test_coll.drop()

def populate():
    clear_data()
    current_app.db.create_collection("test_coll")
    with open("data.json") as file:
        file_data = json.load(file)
    current_app.db.test_coll.insert_many(file_data)
