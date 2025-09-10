from flask import Flask ,request,jsonify

app = Flask(__name__)
#http://127.0.0.1:5000/index                  执行index get
#http://127.0.0.1:5000/index?age=19&pwd=123   执行index get
#http://127.0.0.1:5000/index                       执行index post
#http://127.0.0.1:5000/                       执行index post
@app.route("/index",methods=['POST','GET'])
def index():
    # age = request.args.get("age")
    # pwd = request.args.get("pwd")
    # print(age, pwd)
    # xx=request.form.get("xxx")
    # yy = request.form.get("yyy")
    # print(xx,yy)

    ## print(request.json,type(request.json))
    # print(request.json)

    return jsonify({"status":True,'data':"123456"})
@app.route("/home")
def home():
    return "失败"
if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    app.run(host="127.0.0.1,",port=5000)