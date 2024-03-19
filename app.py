# Flask 
from flask import Flask, render_template, jsonify, request, redirect, session
app = Flask(__name__)

# pyjwt
import jwt

# pymongo DB 연결 
from pymongo import MongoClient 
client = MongoClient('localhost',27017)
db = client.jungleBob

# jwt를 위한 비밀키
SECRET_KEY = "jungleBob"

# 메뉴를 출력 
@app.route("/today")
def home() :
    return render_template('index.html')

#################################### 회원가입 

# 회원가입 화면 출력 
@app.route("/signIn", methods=['GET'])
def signInGet() : 
    return render_template("signin.html")

# 회원가입 요청 
@app.route("/signIn", methods=['POST'])
def signInPost() :
    userId = request.form['signinID'].strip()
    userPw = request.form['signinPW'].strip()
    userName = request.form['signinName'].strip()
    
    userData = db.users.find_one({"id":userId})
    
    if userData == None :
        result = db.users.insert_one({"id":userId, "pw":userPw, "name":userName});
        print(result)
        return jsonify({"msg":"signin success"})
    else :
        return jsonify({"msg":"Fail"})
        
#####################################

#################################### 로그인 
# 로그인 창 띄우기 
@app.route("/login", methods=['GET'])
def loginGet() :
    pass

# 로그인 시도 
@app.route("/login", methods=['POST'])
def loginPost() :
    pass

#####################################

if __name__ == "__main__" :
    app.run("0.0.0.0", port=5000, debug=True)