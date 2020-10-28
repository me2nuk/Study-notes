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