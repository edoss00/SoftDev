#Elizabeth Doss
#SoftDev1 pd1
#K15 -- ?
#2019-10-02

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

head = """
Emory Walsh & Elizabeth Doss -- Flower Power
SoftDev1 pd1
K15 -- ?
2019-10-02
"""

@app.route("/")
def form():
    print("whyyy")
    return render_template("temp.html",
                               header = head)
userN = "mykolyk"
passW = "?"

user = []

@app.route("/auth")
def authenticate():
    print("whyyyyyyy")
    print(url_for('form'))
    print(url_for('authenticate'))
    #print(user)
    user = []
    return redirect(url_for("form"))

@app.route("/disp_login")
def login():
    user.append(request.args['username'])
    user.append(request.args['password'])
    print(user)
    if (user[0] == userN and user[1] == passW):
        return render_template("authTemp.html",
                        username = request.args['username'],
                        password = request.args['password'])
    else:
        user.pop()
        user.pop()
        return render_template("authTempError.html",
                                username = request.args['username'],
                                password = request.args['password'])


if __name__ == "__main__":
    app.debug = True
    app.run()
