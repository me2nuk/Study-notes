from flask import Flask, request # 웹 서버 구축을 위해 사용할 모듈
from selenium import webdriver # XSS를 발생시키기 위해 JS를 실행시킬 셀레니움 모듈
import urllib.parse # URL 인코딩을 하기 위한 모듈

app = Flask(__name__) # Flask 인스턴스 생성

FLAG = 'FLAG' # FLAG TEST

CONFIG = ['headless', 'window-size=1920x1080', 'disable-gpu', 'no-sandbox', 'disable-dev-shm-usage'] # Chrome Options List

def BOT(xss): # BOT 함수 정의

    ChromeOptions = webdriver.ChromeOptions() # ChromeDriver 관련 기능을 설정하기 위해 ChromeOptions 인스턴스 호출

    for _ in CONFIG: # CONFIG 리스트 안에 있는 요소를 반복하면서 가져옵니다.
        ChromeOptions.add_argument(_) # Chrome 실행 옵션 추가
    try: # 예외처리
        driver = webdriver.Chrome('chromedriver.exe', options=ChromeOptions) # chromedriver.exe 실행
        driver.implicitly_wait(3) # 페이지의 요소를 로드될 때 까지 기다립니다.
        driver.set_page_load_timeout(3) # 오류가 발생하기 전 페이지 로드가 완료 될 때 까지 기다립니다.
        driver.get('http://127.0.0.1:8080') # http://127.0.0.1:8080 URL으로 페이지 오픈

        driver.add_cookie({'name':'FLAG', 'value':FLAG}) # FLAG=FLAG 으로 Cookie 생성
        driver.get(f'http://127.0.0.1:8080/xss?xss={urllib.parse.quote(xss)}') # XSS를 발생시키는 페이로드 실행

    except: # 에러 발생하면 실행
        return False # 에러 없이 실행이 되면 거짓을 반환

    driver.quit() # driver를 종료하고 모든 관련 창을 닫습니다.
    return True # 에러 없이 실행이 되면 참을 반환

@app.route('/') # / URL을 생성합니다.
def index(): # index 함수 정의
    return 'hello' # 웹 페이지에 hello 문자열을 반환합니다.

@app.route('/send', methods=['GET']) # /send URL을 생성합니다.
def send(): # send 함수 정의
    if request.method == 'GET': # HTTP 요청 메서드가 GET 방식인지 체크 합니다.
        xss = request.args.get('xss', '') # HTTP REQUEST GET 방식으로 xss 매개변수 받고 없으면 기본값은 '' 으로 반환합니다.
        if BOT(xss): # BOT Function
            return 'Good' # 웹 페이지에 Good를 반환합니다.
        else: # BOT 함수의 반환값이 거짓이라면 실행
            return 'Wrong' # 웹 페이지에 Wrong를 반환합니다.
    else: # HTTP 요청 GET 방식이 아닌 경우 실행
        return 'Method Not Allowed' # 웹 페이지에 Method Not Allowed를 반환합니다.

@app.route('/xss', methods=['GET']) # /xss URL을 생성합니다.
def _xss(): # _xss 함수 정의
    if request.method == 'GET':
        xss = request.args.get('xss', '') # HTTP REQUESTS GET 방식으로 xss 매개변수를 받고 없으면 기본값은 '' 으로 반환합니다.
        if xss: # xss 변수 값이 존재하는지 체크
            return xss # 웹 페이지에 xss 변수를 반환합니다.
        else: # xss 변수 값이 존재하지 않는 경우 실행
            return '?xss=' # 웹 페이지에 ?xss=를 반환합니다.
    else: # HTTP 요청 GET 방식이 아닌 경우 실행
        return 'Metnod Not Allowed' # 웹 페이지에 Method Not Allowed를 반환합니다.

app.run('0.0.0.0', 8080) # 0.0.0.0:8080 OPEN