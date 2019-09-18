from flask import Flask
app = Flask(__name__) #create instance of class Flask


@app.route("/flaskApps") #assign following fxn to run when root route requested

def hello_world():
    print(__name__) #where will this go?
    return "Hablo queso!"

if __name__ == "__main__":
    app.debug = True
    app.run()
