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
            valList.append(float(data[i]['value']))
    return valList

# flask
@app.route("/")
def helloworld():
    clean = cleaner()
    #print(clean)
    return render_template('index.html', clean = clean)

if __name__ == "__main__":
    app.debug = True
    app.run()
