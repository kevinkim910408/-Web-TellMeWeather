from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# mongoDB - pymongo, dnspython 패키지
from pymongo import MongoClient

# sparta@cluster0 (내 db폴더이름@내클러스터이름)
client = MongoClient('mongodb+srv://test:sparta@cluster0.m7jzf.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


# 기본으로 보여줄 index.html 파일
@app.route('/')
def home():
   return render_template('index.html')


# post cityName
@app.route("/search", methods=["POST"])
def city_post():
    db.tellMeWeather.drop();
    city_receive = request.form['cityName_give']
    doc = {
        'cityName': city_receive,
    }
    db.tellMeWeather.insert_one(doc)
    return jsonify({'msg': 'Search Successfully!'})


# get data from db
@app.route("/search", methods=["GET"])
def city_get():
    city_list = list(db.tellMeWeather.find({}, {'_id': False}))
    return jsonify({'msg': city_list})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)