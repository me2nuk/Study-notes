# Python-Flask

<br>

![Flask image](./image/Flask_logo.svg)

# Flask 란

Flask 는 Python 으로 작성된 웹 프레임워크중 하나이며

Flask는 django 에 비해 문법이 단결하고 대형 프로젝트가 아닌이상 쓰기 편하고

Flask로 web server 구축하는 코드는 간단하다.

* * *

```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def Index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = 80)
```

app.route 로 url 을 새로 생성해주고

Hello World! 를 웹페이지에 그대로 출력하게 만들었다.

이와같이 소스코드가 간단하고 속도도 빠르며

Django 와 반대로 심플하고 , 가볍게 설계외었고 개발자들이 원하는 방향으로 쉽게 설계가 가능하다.

## @app.route('')

```py
@app.route('/')
def Index():
    return 'Hello World!'

@app.route('/hello')
def hello():
    return 'Hello'

@app.route('/world')
def world():
    return 'World!'
```

위 처럼 

/world 
/hello 

같은 경로를 새로 생성하기 위해서는

```py
@app.route('')
```

@app.route 안에 원하는 url 을 넣은다음

def 원하는 함수이름(): 으로하고 

자신이 원하는데로 작업하면 된다.

즉 해당 경로로 요청이 올때 실행할 함수를 밑에 작성해야된다.

* * *

## app.run()

__해당 함수는 flask 서버를 시작하기위해서 사용하는 함수이다.__

만약에 run 함수에 아무런 인자를 넣지않는다면

* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

이처럼 기본값으로 서버가 열린다

만약에 다신이 원하는대로 사용하고싶다면

app.run(host = '0.0.0.0' , port = 80)

기본적으로 host(ip) port(포트) 를 수동으로 인자를 넣어 실행할 수 있다.