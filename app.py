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




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)