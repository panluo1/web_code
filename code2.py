import hashlib
from flask import Flask ,request,jsonify

app = Flask(__name__)

@app.route("/bili",methods=['POST'])
def bili():
    """
    请求数据格式要求：{"ordered_string:"......"}
    return
    """
    ordered_string = request.json.get("ordered_string")
    if not ordered_string:
        return jsonify({"status":False,'error':"参数错误"})
    encrypt_string = ordered_string + "560C52CCD56564644644"
    obj = hashlib.md5(encrypt_string.encode('utf-8'))
    sign=obj.hexdigest()
    return jsonify({"status":True,'data':sign})
if __name__ == "__main__":
    app.run()
if __name__ == "__main__":
    app.run(host="127.0.0.1,",port=5000)