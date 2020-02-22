from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostData(postData, functionName):
    if (functionName == "add" or functionName == "subtract" or functionName == "multiply"):
        if ("x" not in postData or "y" not in postData):
            return 301
        else:
            return 200
    elif (functionName == "division"):
        if ("x" not in postData or "y" not in postData):
            return 301
        elif (int(postData["y"]) == 0):
            return 302
        else:
            return 200

class Add(Resource):
    def post(self):
        postData = request.get_json()

        status_code = checkPostData(postData, "add")
        if (status_code != 200):
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
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Subtract(Resource):
    def post(self):
        postData = request.get_json()

        status_code = checkPostData(postData, "subtract")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postData["x"]
        y = postData["y"]
        x = int(x)
        y = int(y)
        ret = x - y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        postData = request.get_json()

        status_code = checkPostData(postData, "multiply")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postData["x"]
        y = postData["y"]
        x = int(x)
        y = int(y)
        ret = x * y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        postData = request.get_json()

        status_code = checkPostData(postData, "division")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postData["x"]
        y = postData["y"]
        x = int(x)
        y = int(y)
        ret = (x * 1.0) / y
        retMap = {
            'Message': ret,
            'Ststus Code': 200
        }
        return jsonify(retMap)


@app.route('/')
def hello_world():
    return "Hello World!"

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/division")

if __name__ == "__main__":
    app.run(host='0.0.0.0')