import requests
import os
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

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