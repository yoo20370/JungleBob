#Flask 
from flask import Flask, render_template
app = Flask(__name__)

from pymongo import MongoClient 
client = MongoClient('localhost',27017)
db = client.jungleBob

@app.route("/")
def home() :
    return render_template('index.html')

from datetime import datetime
@app.route("/today", methods=['GET'])
def today() : 
    date = ""
    date += str(datetime.today().year) + "-"
    date += str(datetime.today().month) + "-"
    date += str(datetime.today().day)

    return render_template('today.html', template_date = date)

if __name__ == "__main__" :
    app.run("0.0.0.0", port=5001, debug=True)