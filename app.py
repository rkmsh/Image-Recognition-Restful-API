from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostData(postData, functionName):
    if (functionName == "add"):
        if ("x" not in postData or "y" not in postData):
            return 301
        else:
            return 200

class Add(Resource):
    def post(self):
        postData = request.get_json()

        status_code = checkPostData(postData, "add")
        if (status_code is not 200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postData["x"]
        y = postData["y"]
        x = int(x)
        y = int(y)
        ret = x + y
        retMap = {
            'Sum': ret,
            'Ststus Code': 200
        }
        return jsonify(retMap)

class Subtract(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass


@app.route('/')
def hello_world():
    return "Hello World!"

api.add_resource(Add, "/add")

if __name__ == "__main__":
    app.run(debug=True)