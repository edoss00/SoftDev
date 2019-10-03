#Elizabeth Doss
#SoftDev1 pd1
#K15 -- ?
#2019-10-02

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

head = """
Emory Walsh & Elizabeth Doss -- Flower Power
SoftDev1 pd1
K15 -- ?
2019-10-02
"""

@app.route("/")
def form():
    return render_template("temp.html",
                               header = head)
userN = "mykolyk"
passW = "?"

user = []

@app.route("/auth")
def authenticate():
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
    
@app.route('/logout')
def log_out():
    button = request.args['LogOut']
    if button == 'logout':
        user.pop()
        user.pop()
    return redirect('http://127.0.0.1:5000')


if __name__ == "__main__":
    app.debug = True
    app.run()
