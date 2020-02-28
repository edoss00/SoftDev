from pymongo import MongoClient
from bson.json_util import loads
import json

c = MongoClient()
db = c.test_database
restaurants = db.restaurants
restaurants.drop()

f = open("primer-dataset.json","r")
rString = f.readlines()
for x in rString:
    restaurants.insert_one(loads(x))
