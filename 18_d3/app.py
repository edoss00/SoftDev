from flask import Flask, render_template
import json
app = Flask(__name__)

# parses json file
def cleaner():
    data = []
    list = []
    with open('static/gdp.json', 'r') as file:
        data = json.loads(file.read())[1]
        for i in range(len(data)):
            list.append({'date': data[i]['date'], 'value': data[i]['value']})
    return list

# flask
@app.route("/")
def helloworld():
    print(__name__)
    clean = cleaner()
    return render_template('index.html', clean = clean)

if __name__ == "__main__":
    app.debug = True
    app.run()
