# Amanda "Amber" Chen, Elizabeth Doss (Team The Riftbreakers)
# SoftDev2 pd1
# K18 -- Come Up For Air
# 2020-04-20

from flask import Flask, render_template
import json
app = Flask(__name__)

# parses json file
def cleaner():
    data = []
    valList = []
    with open('static/gdp.json', 'r') as file:
        data = json.loads(file.read())[1]
    for i in range(len(data)):
        valList.append([int(data[i]['date']),float(data[i]['value'])])
    # print(valList[::-1])
    return valList[::-1]

# flask
@app.route("/")
def helloworld():
    clean = cleaner()
    print(clean)
    return render_template('index.html', gdp = clean)

if __name__ == "__main__":
    app.debug = True
    app.run()
