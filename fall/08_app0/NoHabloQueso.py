#Elizabeth Doss
#SoftDev1 pd1
#K8 -- Lemme Flask You Sump’n
#2019-09-18

#prepares flask
from flask import Flask
app = Flask(__name__) #create instance of class Flask

#normal route
@app.route("/") #assign following fxn to run when root route requested
def queso():
    print(__name__ + "norm") #prints in terminal
    return "No hablo queso!" #prints on webpage

#route 1
@app.route("/escribo") #if added to url, opens new page
def food1():
    print(__name__ + "test1")
    return "No escribo queso!"

#route 2
@app.route("/escucho") #if added to url, opens new page
def food2():
    print(__name__ + "test2")
    return "No escucho queso!"

#route 3
@app.route("/soy") #if added to url, opens new page
def food3():
    print(__name__ + "test3")
    return "No soy queso!"

#main
if __name__ == "__main__":
    app.debug = True
    app.run()
