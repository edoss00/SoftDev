#Elizabeth Doss
#SoftDev1 pd1
#K16 -- Oh yes, perhaps I do...
#2019-10-03

from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

head = """
Emory Walsh & Elizabeth Doss -- Flower Power
SoftDev1 pd1
K16 --  Oh yes, perhaps I do…
2019-10-03
"""

#random code sequence
app.secret_key="asdfghjkl"

#built in username and password
userN = "mykolyk"
passW = "?"
loggedIn = False

#root
@app.route("/")
def homepage():
    #print("/")
    #print(session)
    #if 'user' in session:
    if loggedIn == True:
        return redirect("/welcome")
    return render_template("homepageTemp.html",
                           header=head)

#welcome if logged in
@app.route("/welcome")
def hi():
    #print("/welcome")
    return render_template("welcomeTemp.html")

#tell that logged out
@app.route("/loggedout")
def logout():
    #print("/loggedout")
    loggedIn = False
    session.pop('user')
    session.pop('pass')
    return render_template("logOut.html")


#decides if correct credentials
@app.route("/auth")
def authenticate():
    #print("/auth")
    session['user'] = request.args['username']
    session['pass'] = request.args['password']
    if (session['user'] == userN and session['pass'] == passW) :
        loggedIn = True
        return redirect ("/welcome")
    else:
       loggedIn = False
       return redirect ("/error")

@app.route("/error")
def errorPath():
    #print("/error")
    if (userN != session['user']):
        session.pop("user")
        session.pop("pass")
        print("done")
        return render_template("errorUser.html")
    session.pop("user")
    session.pop("pass")
    return render_template("errorPass.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
