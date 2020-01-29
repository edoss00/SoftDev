# Elizabeth Doss
# SoftDev1 pd1
# K10 -- Jinja Tuning
# 2019-09-22   

from flask import Flask, render_template 
app = Flask(__name__)

#initial page
@app.route("/")
def helloWorld():
        return "Hi there, add /occupyflaskst to the URL for something cool!"

################################
#code from K6 to produce random occupation
import random

occupations = {}
links = {}
f = open("occupations.csv","r")
fString = f.readlines()
#print(fString)
fString = fString[1:len(fString) - 1]
for s in fString:
        fList = s.rsplit(",",4)
        fList[1] = fList[1].strip("\n")
        fList[0] = fList[0].replace('"', '')
        occupations[fList[0]] = float(fList[1])
        links[fList[0]] = fList[2]
#print(links)
#print(occupations)
fNewList = []
for keys,values in occupations.items():
        small = [keys,values]
        fNewList.append(small)
        
def randomOcc():
    r = random.randint(1, 998) / 10.0
    for s in fNewList:
        r -= float(s[1])
        if (r <= 0):
            return s[0]
################################

#create app route that goes to occupations html file
@app.route('/occupyflaskst')
def occs_template():
    return render_template('occTemp.html',
                           title = 'Occupations', #template title
                           randOcc = randomOcc(), #randomly choose a job
                           occLinks = links,
                           collection = occupations #creates dict of occupations and percentages
                           #creates dict of occupations and links
                           )

if __name__ == "__main__":
    app.debug = True
    app.run()
