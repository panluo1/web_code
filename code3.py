import hashlib
from flask import Flask ,request,jsonify

app = Flask(__name__)

def get_user_dict():
    info_dict = {}
    with open('db.txt','r',encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            token,name = line.split(",")
            info_dict[token] = token
    return info_dict
@app.route("/bili",methods=['POST'])
def bili():
    """
    请求数据格式要求：{"ordered_string:"......"}
    return
    """
    token = request.args.get("token")
    if not token:
       return jsonify({"status":False,'error':"认证失败"})
    user_dict = get_user_dict()
    if token in user_dict:
        return jsonify({"status": False, 'error': "认证失败"})
    ordered_string = request.json.get("ordered_string")
    if not ordered_string:
        return jsonify({"status":False,'error':"参数错误"})
    encrypt_string = ordered_string + "560C52CCD56564644644"
    obj = hashlib.md5(encrypt_string.encode('utf-8'))
    sign=obj.hexdigest()
    return jsonify({"status":True,'data':sign})

if __name__ == "__main__":
    app.run(host="127.0.0.1,",port=5000)