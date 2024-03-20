import requests
from bs4 import BeautifulSoup

# IP
from var import IP

# MongoDB ID/PW
from var import ID
from var import PW
from var import DBPORT

from pymongo import MongoClient 
client = MongoClient('mongodb://' + ID + ':' + PW + '@' + IP, DBPORT)
db = client.jungleBob
menus = db["menus"]

url = "https://dorm.kyonggi.ac.kr:446/Khostel/mall_main.php?viewform=B0001_foodboard_list&board_no=1"

response = requests.get(url)
print('응답코드: ', response.status_code)
response.raise_for_status()

html = response.content.decode('euc-kr')
soup = BeautifulSoup(html, 'html.parser')

# 경기드림타워 기숙사 메뉴 스크래핑
dream_tower = soup.select('table.boxstyle02 > tbody > tr')
# 일요일, 토요일 제거
del dream_tower[0]
del dream_tower[5]

for dreamtower in dream_tower:

  #날짜 정보 가져오기
  date = dreamtower.select_one('th > a').text.strip()
  day = date.split()[1]
  date = date.split()[0]

  # 점심 DB 저장
  lunch = dreamtower.select_one('td:nth-child(3)').text.strip()
  dreamtower_menu = {
    'place': '경기드림타워',
    'lunch': True,
    'menu': lunch,
    'date': date,
    'day': day
  }
  db.menus.insert_one(dreamtower_menu)

  # 저녁 DB 저장
  dinner = dreamtower.select_one('td:nth-child(4)').text.strip()
  dreamtower_menu = {
    'place': '경기드림타워',
    'lunch': False,
    'menu': dinner,
    'date': date,
    'day': day
  }
  db.menus.insert_one(dreamtower_menu)
