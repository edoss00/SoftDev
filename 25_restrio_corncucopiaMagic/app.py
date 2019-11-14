# Elizabeth Doss
# SoftDev1 pd1
# K25 -- Getting More REST
# 2019-11-13

from flask import Flask, render_template, request, redirect, url_for
import json
from urllib.request import urlopen
app = Flask(__name__)


@app.route("/")
def root():
    return render_template('root.html')

#GNews API
#API_KEY: b0aec2d3195147058f97981de000e4ad
#https://newsapi.org/v2/top-headlines?country=COUNTRY&apiKey=API_KEY
@app.route("/news")
def news():
    print(app)
    u = urlopen("https://newsapi.org/v2/top-headlines?country=us&apiKey=b0aec2d3195147058f97981de000e4ad")
    response = u.read();
    info = json.loads(response);
    return render_template('news.html',
                           article = info['articles'][0]['title'],
                           desc = info['articles'][0]['description'],
                           link = info['articles'][0]['url'],
                           pic = info['articles'][0]['urlToImage'],
                           content = info['articles'][0]['content'])

#College Scorecard API
#API_KEY: wIJwxhjDafbH3R4tmjTkCx1bch8T2fdoHblbjmzW
#https://api.data.gov/ed/collegescorecard/v1/schools.json?{parameters}&api_key={key}
@app.route("/college")
def college():
    print(app)
    u = urlopen("https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&_fields=id,school.name,2017.student.size&api_key=wIJwxhjDafbH3R4tmjTkCx1bch8T2fdoHblbjmzW")
    response = u.read();
    info = json.loads(response);
    return render_template('college.html',
                           name0 = info['results'][0]['school.name'],
                           size0 = info['results'][0]['2017.student.size'],
                           name1 = info['results'][1]['school.name'],
                           size1 = info['results'][1]['2017.student.size'],
                           name2 = info['results'][2]['school.name'],
                           size2 = info['results'][2]['2017.student.size'],
                           name3 = info['results'][3]['school.name'],
                           size3 = info['results'][3]['2017.student.size'])

#MET Museum Collections API
#No API key needed
#https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}
@app.route("/art")
def art():
    print(app)
    u = urlopen("https://collectionapi.metmuseum.org/public/collection/v1/objects/435983")
    response = u.read();
    info = json.loads(response);
    return render_template('art.html',
                           pic = info['primaryImageSmall'],
                           depo = info['department'],
                           title = info['title'],
                           artist = info['artistDisplayName'],
                           finished = info['objectDate'],
                           medium = info['medium'])


if __name__ == "__main__":
    app.debug = True
    app.run()
