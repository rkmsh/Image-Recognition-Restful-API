from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hithere')
def hi_there_everyone():
    return "I just hit /hithere!"

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