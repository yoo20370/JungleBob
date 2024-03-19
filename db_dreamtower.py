import requests
from bs4 import BeautifulSoup

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

  lunch = dreamtower.select_one('td:nth-child(3)').text.strip()
  print(lunch)

  dinner = dreamtower.select_one('td:nth-child(4)').text.strip()

  lunch = {
    'name': '경기드림타워_점심',
    'day': date,
    'menu': lunch
  }
  dinner = {
    'name': '경기드림타워_저녁',
    'day': date,
    'menu': dinner
  }

  print(lunch)