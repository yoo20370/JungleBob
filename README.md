# 정글밥 (JungleBob)

정글밥은 경기대학교 식당의 메뉴를 크롤링하여 보여주고, 친구들과 함께 어떤 식당에서 식사할지 선택할 수 있는 웹 서비스입니다.

## 기술 스택

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)

## 주요 기능

- 학교 식당 메뉴 크롤링 및 표시
- 일일 식사 장소 선택 및 공유
- 사용자 회원가입 및 로그인
- 전날 식사 내역 확인
- 식당 위치 지도 표시

## 프로젝트 구조

```
.
├── .venv/              # 가상 환경 디렉토리
├── static/             # 정적 파일 디렉토리 (CSS, JavaScript, 이미지 등)
├── templates/          # HTML 템플릿 파일들
├── app.py              # 메인 애플리케이션 파일
├── db_dreamtower.py    # 경기드림타워 식당 메뉴 크롤링 스크립트
└── var.py              # 환경 변수 설정 파일
```

## 설치 및 실행

1. 레포지토리를 클론합니다.
   ```
   git clone https://github.com/your-username/jungle-bob.git
   cd jungle-bob
   ```

2. 가상 환경을 생성하고 활성화합니다.
   ```
   python -m venv .venv
   source .venv/bin/activate  # Windows의 경우: .venv\Scripts\activate
   ```
3. MongoDB를 설치하고 실행합니다.

4. `var.py` 파일에 필요한 환경 변수를 설정합니다.
   ```python
   SECRET_KEY = 'your_secret_key'
   PORT = 5000
   IP = 'your_server_ip'
   ID = 'mongodb_username'
   PW = 'mongodb_password'
   DBPORT = 27017
   ```

5. 애플리케이션을 실행합니다.
   ```
   python app.py
   ```

6. 웹 브라우저에서 `http://localhost:5000`으로 접속합니다.

## 주요 라우트

- `/`: 메인 페이지 (로그인 페이지로 리다이렉트)
- `/login`: 로그인 페이지
- `/signIn`: 회원가입 페이지
- `/today`: 오늘의 메뉴 및 식사 선택 페이지
- `/mypage`: 사용자 마이페이지 (전날 식사 내역 확인)
- `/map`: 식당 위치 지도

