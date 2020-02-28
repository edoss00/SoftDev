from pymongo import MongoClient
from bson.json_util import loads
import json

c = MongoClient()
db = c.test_database
restaurants = db.restaurants

f = open("primer-dataset.json","r")
rString = f.read()
t = loads(rString)

# rList = rString.split('\n')

# for r in rList:
#print(rList[0])
    # t = loads(r)
    #print(type(t))
restaurants.insert_many(t)
