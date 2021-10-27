import requests
import os

from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

# API 역할을 하는 부분
# 음식 리스트 가져오기
@app.route('/api/list', methods=['GET'])
def show_foods():
    show_food = list(db.korfoodlist.find({}, {'_id': False}))
    return jsonify({'foods': show_food})

# HTML 화면 보여주기
@app.route('/')
def info():
    return render_template('page1.html')

@app.route('/page3')
def home():
    return render_template('page3.html')

# 푸드 food DB에 넣기
def insert_food():
    path = 'static/food'
    food_list = os.listdir(path)
    for item in food_list:
        img = path +'/'+ item
        doc = {
            'img': img,
        }
        db.korfoodlist.insert_one(doc)

# 기존 korfoodlist 콜렉션을 삭제하고, 새로 DB에 저장합니다.
def insert_all():
    db.korfoodlist.drop()  # korfoodlist 콜렉션을 모두 지워줍니다.

    insert_food()


# 실행하기
insert_all()


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)