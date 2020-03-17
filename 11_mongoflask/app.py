# Yaru && EDoss
# SoftDev1 pd1
# K11: Ay Mon Go Git It From Yer Flask
# 2020-03-10

from flask import Flask, request, render_template
from bson.json_util import loads
from pymongo import MongoClient

app = Flask(__name__)
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
  eplist = ["Season: {}  Episode: {}".format(season, number)]
  eplist.append("Results Found: {}".format(results.count()))
  for x in results:
    eplist.append("Episode Title: {}".format(x["name"]))
    if(x["summary"] == "" or x["summary"] is None):
      eplist.append("No summary available.")
    else:
      eplist.append(x["summary"][3:-4] + "\n")
  return eplist


# ------------------------ flaskin ----------------------------

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/bigbang')
def bigbang():
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    season = request.args.get('season')
    print(season)
    episode = request.args.get('episode')
    print(episode)
    print(findEpisode(1,1))
    return render_template( 'template.html', xxx = findEpisode(season, episode))

if __name__ == "__main__":
    app.debug = True # this automatically reloads any changes
    app.run(host='0.0.0.0') # this runs the website
