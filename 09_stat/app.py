# Elizabeth Doss
# SoftDev1 pd1
# K9 -- ’Tis Not a Race -- But You Will Go Faster
# 2019-09-22   

from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
def helloWorld():
	return "hi there friend"

@app.route("/my_foist_template")
def temp():
	coll = [0,1,1,2,3,5,8]
	return render_template(
		"my_foist_template.html",
		collection = coll,
		foo="what am I doing"
	)

if __name__ == "__main__":
	app.debug = True
	app.run()
