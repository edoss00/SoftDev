#prepares flask
from flask import Flask, render_template, request
from bson.json_util import loads
from pymongo import MongoClient

app = Flask(__name__) #create instance of class Flask

client = MongoClient()
db = client.yarn
info = db.info
with open( 'data.json', 'r') as file:
    content = file.readlines()
    if( info.count() == 0):
        for line in content:
            info.insert_one( loads( line))
        for x in info.find({}):
            temp = x[ '_embedded'][ 'episodes']
            for y in temp:
                db.episodes.insert_one( y)

def findEpisode(season, number):
  '''Episode name from the specified season and episode number.'''
  results = db.episodes.find({ "season": season, "number": number })
  #formatting printed results
  print("Season: {}  Episode: {}".format(season, number))
  print("Results Found: {}".format(results.count()))
  print()
  for x in results:
    print("Episode Title: {}".format(x["name"]))
    if(x["summary"] == "" or x["summary"] is None):
      print("No summary available.")
    else:
      print(x["summary"][3:-4] + "\n")


def onAir(airdate):
  '''Episode from the specified airing date.'''
  results = db.episodes.find({ "airdate": airdate })
  #formatting printed results
  print("Given Date: {}".format(airdate))
  print("Results Found: {}".format(results.count()))
  print()
  for x in results:
    print("Season {} Episode {}: {}".format(x["season"], x["number"], x["name"]))
    if(x["summary"] == "" or x["summary"] is None):
      print("No summary available." + "\n")
    else:
      print(x["summary"][3:-4] + "\n")


print("------ Find an episode by giving a season and episode number. ------")
season = input("Please enter a season: ")
number = input("Please enter an episode number: ")
while(not season.isnumeric()):  #checking for non-numbers
  season = input("Please enter a valid number: ")
while(not number.isnumeric()):
  number = input("Please enter a valid number: ")
print()


print("------ Find episode(s) aired on a given date. ------")
year = input("Please enter a four-year between 1999 and 2020: ")
while(not year.isnumeric() or (int(year) > 2020) or (int(year) < 1999)):  #checking for valid years
  year = input("Please enter a valid four-digit year: ")
month = input("Please enter a month (with a 0 in front of single-digit months): ")
while(not(len(month) == 2) or not month.isnumeric() or int(month) > 12 or int(month) < 1):  #checking for valid month (with the 0)
  month = input("Please enter a valid month (with a 0 in front of single-digit months): ")
day = input("Please enter a day (with a 0 in front of single-digit days): ")
while(not day.isnumeric() or not(len(day) == 2) or int(day) > 31 or int(day) < 1):  #checking for valid dates (with the 0)
  day = input("Please enter a valid day (between 1 and 31, and with a 0 in front of single-digit days): ")
print()

#normal route
@app.route("/") #assign following fxn to run when root route requested
def bigbang():
    print(__name__) #prints in terminal
    return render_template("bigbang.html")

#main
if __name__ == "__main__":
    app.debug = True
    app.run()





# {"id":2913,"url":"http://www.tvmaze.com/episodes/2913/the-big-bang-theory-1x01-pilot","name":"Pilot","season":1,"number":1,"airdate":"2007-09-24","airtime":"20:30","airstamp":"2007-09-25T00:30:00+00:00","runtime":30,"image":{"medium":"http://static.tvmaze.com/uploads/images/medium_landscape/4/12368.jpg","original":"http://static.tvmaze.com/uploads/images/original_untouched/4/12368.jpg"},"summary":"<p>Is a comedy about brilliant physicists, Leonard and Sheldon, who are the kind of \"beautiful minds\" that understand how the universe works. But none of that genius helps them interact with people, especially women. All this begins to change when a free-spirited beauty named Penny moves in next door. Sheldon, Leonard's roommate, is quite content spending his nights playing Klingon Boggle with their socially dysfunctional friends, fellow Cal Tech scientists Wolowitz and Koothrappali. However, Leonard sees in Penny a whole new universe of possibilities... including love.</p>","_links":{"self":{"href":"http://api.tvmaze.com/episodes/2913"}}},
