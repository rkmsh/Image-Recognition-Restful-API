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
    retJson = {
        'field1': 'abc',
        'field2': 'def'
    }

    return jsonify(retJson)

if __name__ == "__main__":
    app.run(debug=True)