# Flask 
from flask import Flask, render_template, jsonify, request, redirect
app = Flask(__name__)

# pyjwt
import jwt

# pymongo DB 연결 
from pymongo import MongoClient 
client = MongoClient('localhost',27017)
db = client.jungleBob

# jwt를 위한 비밀키
SECRET_KEY = "jungleBob"

@app.route("/")
def home() :
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def loginCheck() :
    userId = request.form['userId']
    userPw = request.form['userPw']
    # 1. 토큰이 함께 전송 됐는지 확인한다. 
    # 1-1. 토큰이 있는 경우 DB에 접근할 필요 X
    # 1-2. 토큰이 없는 경우 로그인 아이디와 비밀번호를 확인하고 토큰을 발행해서 클라이언트에 전달한다. ( 클라이언트에서 쿠키나 로컬 저장소에 저장한다. )
    userData = db.users.find_one({"id":userId},{"_id":False})

    if userId == userData['id'] and userPw == userData['password'] :

        payload = {
            "id":userData['id'],
            "pw":userData['password']
        }
        token =  jwt.encode(payload , SECRET_KEY , "HS256")
        return jsonify({"msg":"create token", "token": token})        

    # 토큰으로 로그인했는데 로그인 창으로 오는 경우 redirect로 홈으로 이동시킨다. 
    return redirect('http://localhost:5000/')
    

if __name__ == "__main__" :
    app.run("0.0.0.0", port=5000, debug=True)