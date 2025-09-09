import flask
from  flask import Flask, request

app=flask.Flask(__name__)
#{"xx":123,"yy":999}
#get请求访问
@app.route("/index",methods=['POST',"GET"])
def index():
    age=request.args.get("age")
    pwd = request.args.get("pwd")
    print(age, pwd)

    xx=request.form.get("xx")
    yy=request.form.get("yy")
    print(xx, yy)

    print(request.json)
    return "OK"


@app.route("/home")
def home():
    return "NO"
if __name__=="__main__":
    app.run()