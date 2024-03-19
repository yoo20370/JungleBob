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

# 메인 페이지
from datetime import datetime
def getDate():
    date = ""
    date += str(datetime.today().year) + "-"
    month = datetime.today().month
    if (month < 10):
        date += "0" + str(month) + "-"
    else:
        date += str(month) + "-"
    date += str(datetime.today().day)

    return date

@app.route("/today", methods=['GET'])
def today() : 
    # 시스템 날짜 가져와 년-월-일 출력
    # 이후 날짜 비교를 위해 date 변수 그대로 사용
    date = getDate()
    day = datetime.today().weekday() ## 요일
    
    ## 기숙사 식당 메뉴 가져오기
    ### 점심
    dt_l_record = db.menus.find_one({"date": date, "place": "경기드림타워", "lunch": True})
    dt_l_menu = dt_l_record['menu']
    dt_l_menu = dt_l_menu.replace('\r\n', ', ')
    print(dt_l_menu)
    ### 저녁
    dt_d_record = db.menus.find_one({"date": date, "place": "경기드림타워", "lunch": False})
    dt_d_menu = dt_d_record['menu']
    dt_d_menu = dt_d_menu.replace('\r\n', ', ')
    print(dt_d_menu)

    # 경슐랭 메뉴 
    kcl_menu = "돈가스, 김밥, 덮밥, 한식, 햄버거, 타코"

    # E-스퀘어 메뉴
    esq_menu = "라면, 김밥, 덮밥, 국수, 돈까스, 아이스크림"

    return render_template('today.html', 
                           template_date = date,
                           template_dt_lunch_menu = dt_l_menu, template_dt_dinner_menu = dt_d_menu,
                           template_kcl_menu = kcl_menu, template_esq_menu = esq_menu)


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
    app.run("0.0.0.0", port=5001, debug=True)