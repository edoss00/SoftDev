from pymongo import MongoClient
import json

c = MongoClient()
db = c.test_database
restaurants = db.restaurants

f = open("primer-dataset.json","r")
rString = f.read()
# print(rString)

rList = rString.split('\n')

for r in rList:
#print(rList[0])
    t = json.loads(r)
    #print(type(t))
    restaurants.insert_one(t)
