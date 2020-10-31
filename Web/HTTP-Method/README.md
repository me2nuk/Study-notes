# HTTP method

### HTTP method 란?

<br>

__Client 측에서 Server 에 어떠한 목적을 가지고 요청을 하기위해있는 수단__

* * *

## HTTP method 종류

```
GET
PUT
POST
HEAD
TRACE
PATCH
DELETE
CONNECT
OPTIONS
```

## GET

[공식 문서 HTTP GET](https://tools.ietf.org/html/rfc2616#section-9.3)

GET 메서드는 모든 정보를 검색하고 
Requeest-URL 로 식별됩니다.

해당 GET는 필요없이 캐시된 엔티티를 새고 고칠 수 있도록하며 여러 요청 또는 클라이언트가 이미 보유한 데이터를 전송하기위해 있다.

클라이언트쪽에서 Url 로 데이터를 받아 정보를 얻는다.

GET 방식으로 데이터를 전달하기 위해서는 ? 로 시작하고
& 로 구분하여야한다.

![Google Method Get](../image/GET_Google.png)

위처럼 google.com 에서 '안녕' 이라고 검색하니 GET 방식으로 여러 데이터를 주고받는것이 보인다.

__다른 예를 사용한다면__

예)__https://google.com?id=hello&pw=world__

예시의 경우
google.com 도메인에서 GET 방식으로 
id 라는 키값에는 hello 값이 들어있고
pw 라는 키값에는 world 값이 들어있다.

PHP 경우 
```PHP
$uid = $_GET['id'];
$upw = $_GET['pw'];
echo $uid."<br>";
echo $upw;
```

python-flask 경우

```py

from flask import Flask
from flask import request
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
 
    uid = request.args.get('id','')
    upw = request.args.get('pw','')
    return uid+"<br>"+upw
```

등등 각 언어들로 HTTP method GET 방식으로 전송되는 데이터를 받아 처리하면된다.