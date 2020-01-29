#Elizabeth Doss
#SoftDev1 pd1
#K12 -- ECHO Echo echo
#2019-09-26

#import necessary packages
from flask import Flask, render_template, request
app = Flask(__name__)

#initial page contains text box to enter username
@app.route("/")
def hello_world():
    print(__name__)
    #print(request)
    return render_template("form.html") #uses template form.html

#follows app route upon pressing submit
@app.route("/auth", methods=["POST"])
def authPage():
    username = request.args["username"] #stores inputted username
    request_method = request.method #stores the method by which requests are made (always GET)
    #print statements to test out request methods
    #print(request.args)
    #print(request.method)
    #print(request)
    #print(request.headers)
    return render_template("response.html", #uses template response.html
                            username=username,
                            request_method=request_method
                            )

if __name__ == "__main__":
    app.debug = True
    app.run()
