from pprint import pprint
from pymongo import MongoClient

c = MongoClient()
db = c.test_database
restaurants = db.restaurants

# All restaurants in a specified borough.
def find_borough(b):
	cursor = restaurants.find({ "borough": b })
	for c in cursor:
		pprint(c)

#find_borough("Bronx")

# All restaurants in a specified zip code.
def find_zip(z):
	cursor = restaurants.find({ "address.zipcode": z})
	for c in cursor:
		pprint(c)

#find_zip("10028")

# All restaurants in a specified zip code and with a specified grade.
def find_zip_grade(z, g):
	cursor = restaurants.find({ "address.zipcode": z, "grades.grade": g})
	for c in cursor:
		pprint(c)

find_zip_grade("10028","A")

# All restaurants in a specified zip code with a score below a specified threshold.
def find_zip_lograde(z, g):
	cursor = restaurants.find({ "address.zipcode": z, "grades.grade": {"$gt":g}})
	for c in cursor:
		pprint(c)

find_zip_lograde("10028","B")

# Something more clever.
# All restaurants in specified zip code with names containing specified string.
def  find_zip_letter(z, n):
	cursor = restaurants.find({"address.zipcode": z, "name": re.compile(n)})
	for c in cursor:
		pprint(c)

find_zip_letter("10459","King")
