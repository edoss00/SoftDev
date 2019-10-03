#Elizabeth Doss
#SoftDev1 pd1
#K15 -- ?
#2019-10-03

from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

head = """
Emory Walsh & Elizabeth Doss -- Flower Power
SoftDev1 pd1
K15 -- ?
2019-10-03
"""

#random code sequence
app.secret_key="asdfghjkl"

#built in username and password
userN = "mykolyk"
passW = "?"

#homepage where prompted with log in
@app.route("/")
def start():
    #print("whyyy")
    return render_template("temp.html",
                           header = head)

#redirects to login page
@app.route("/auth")
def authenticate():
    #print(url_for('form'))
    #print(url_for('authenticate'))
    #print(user)
    if ("user" in session):
        return redirect(url_for("start"))

#log out page after successful log in
@app.route("/loggedout")
def logout():
    #print("wowow")
    return render_template("logOut.html")

#login - contains three possible routes
@app.route("/disp_login")
def login():
    session['user'] = request.args['username']
    session['pass'] =request.args['password']
    #if accurate
    if (userN == session['user'] and passW == session['pass']):
        return render_template("authTemp.html",
                        username = request.args['username'],
                        password = request.args['password'])
    #if username incorrect
    elif (userN != session['user']):
        return render_template("errorUser.html")
    #if password incorrect
    else:
        return render_template("errorPass.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
