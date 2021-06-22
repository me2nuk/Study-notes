from flask import Flask, request
from selenium import webdriver
import urllib.parse

app = Flask(__name__)

FLAG = 'FLAG'

CONFIG = ['headless', 'window-size=1920x1080', 'disable-gpu', 'no-sandbox', 'disable-dev-shm-usage'] # Chrome Options

def BOT(xss):

    ChromeOptions = webdriver.ChromeOptions()

    for _ in CONFIG:
        ChromeOptions.add_argument(_) # Chrome 실행 옵션 추가
    try:
        driver = webdriver.Chrome('chromedriver.exe', options=ChromeOptions)
        driver.implicitly_wait(3) # 페이지의 요소를 로드될 때 까지 기다립니다.
        driver.set_page_load_timeout(3) # 오류가 발생하기 전 페이지 로드가 완료 될 때 까지 기다립니다.
        driver.get('http://127.0.0.1:8080')

        driver.add_cookie({'name':'FLAG', 'value':FLAG}) # FLAG=FLAG 으로 Cookie 생성
        driver.get(f'http://127.0.0.1:8080/xss?xss={urllib.parse.quote(xss)}') # XSS를 발생시키는 페이로드 실행

    except:
        return False

    driver.quit() # driver를 종료하고 모든 관련 창을 닫습니다.
    return True

@app.route('/')
def index():
    return 'hello'

@app.route('/send', methods=['GET'])
def send():
    if request.method == 'GET':
        xss = request.args.get('xss', '') # HTTP REQUEST GET 방식으로 xss 매개변수 받고 없으면 기본값은 '' 으로 반환합니다.
        if BOT(xss): # BOT Function
            return 'Good'
        else:
            return 'Wrong'
    else:
        return 'Method Not Allowed'

@app.route('/xss', methods=['GET'])
def _xss():
    if request.method == 'GET':
        xss = request.args.get('xss', '') # HTTP REQUESTS GET 방식으로 xss 매개변수를 받고 없으면 기본값은 '' 으로 반환합니다.
        if xss:
            return xss
        else:
            return '?xss='
    else:
        return 'Metnod Not Allowed'

app.run('0.0.0.0', 8080) # 0.0.0.0:8080 OPEN