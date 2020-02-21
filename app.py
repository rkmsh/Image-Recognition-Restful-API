from flask import Flask, jsonify, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hithere')
def hi_there_everyone():
    return "I just hit /hithere!"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    dataDict = request.get_json()
    if( "x" or "y" not in dataDict):
        return "ERROR", 305
    x = dataDict["x"]
    y = dataDict["y"]
    z = x + y

    retJson = {
        "z": z
    }

    return jsonify(retJson), 200

@app.route('/bye')
def bye():
    age = 4 * 5
    retJson = {
        'Name': 'Bug Hunter',
        'Age': age,
        "Phones": [
            {
                "PhoneName": "Iphone X",
                "PhoneNumber": "888888888"
            },
            {
                "PhoneNumber": "Nokia",
                "PhoneNumber": "8888888888"
            }
        ]
    }

    return jsonify(retJson)

if __name__ == "__main__":
    app.run(debug=True)