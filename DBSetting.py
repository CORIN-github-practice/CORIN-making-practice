import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


# DB에 저장할 영화인들의 출처 url을 가져옵니다.
# def get_urls():
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     data = requests.get('https://movie.naver.com/movie/sdb/rank/rpeople.nhn', headers=headers)
#
#     soup = BeautifulSoup(data.text, 'html.parser')
#
#     trs = soup.select('#old_content > table > tbody > tr')
#
#     urls = []
#     for tr in trs:
#         a = tr.select_one('td.title > a')
#         if a is not None:
#             base_url = 'https://movie.naver.com/'
#             url = base_url + a['href']
#             urls.append(url)
#
#     return urls


# 출처 url로부터 영화인들의 사진, 이름, 최근작 정보를 가져오고 mystar 콜렉션에 저장합니다.
# def insert_star(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     data = requests.get(url, headers=headers)
#
#     soup = BeautifulSoup(data.text, 'html.parser')
#
#     name = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a').text
#     img_url = soup.select_one('#content > div.article > div.mv_info_area > div.poster > img')['src']
#     recent_work = soup.select_one(
#         '#content > div.article > div.mv_info_area > div.mv_info.character > dl > dd > a:nth-child(1)').text
#
#     doc = {
#         'name': name,
#         'img_url': img_url,
#         'recent': recent_work,
#         'url': url,
#         'like': 0
#     }
#
#     db.mystar.insert_one(doc)
#     print('완료!', name)

# 나라별 푸드 food DB에 넣기
def insert_food(country):
    for i in range(1, 17):
        img = 'static/'+country+'/'+country+' ('+str(i)+').jpg'
        doc = {
            'img': img,
            'round': 1,
        }
        db.korfoodlist.insert_one(doc)

# 기존 korfoodlist 콜렉션을 삭제하고, 새로 DB에 저장합니다.
def insert_all():
    db.korfoodlist.drop()  # korfoodlist 콜렉션을 모두 지워줍니다.
    country = 'kor'
    insert_food(country)


# 실행하기
insert_all()