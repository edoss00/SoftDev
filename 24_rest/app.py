#Elizabeth Doss
#SoftDev1 pd1
#K24 -- A RESTful Journey Skyward
#2019-11-12

#prepares flask
from flask import Flask, render_template, request
#import urllib
from urllib.request import urlopen

app = Flask(__name__) #create instance of class Flask

def getStars():
    data = urlopen("https://api.nasa.gov/planetary/apod?api_key=kmnrWrniE29xLftxSwJQs8PdYbMRMPvIMGQn7ZIh")
    pic = data.read()
    return pic



#normal route
@app.route("/") #assign following fxn to run when root route requested
def stars():
    return render_template("nasa.html",
                           pic = getStars())

#main
if __name__ == "__main__":
    app.debug = True
    app.run()
