from flask import Flask


app = Flask(__name__)

@app.route("/hello")
def hello():
    result = {"code": 200,
            "msg": "hello",
            "data": None}
    return result


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8888, debug=True)