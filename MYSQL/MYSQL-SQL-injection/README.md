# sql injection


### sql injection 이란?

> 데이터베이스를 사용하는 과정에서 의도치 않은 데이터를 주입하는것

sql는 데이터베이스의 데이터들을 관리하기위해 설계된 프로그래밍 언어이다.

자주쓰이는 sql 종류는
mysql , mssql , mongo 등등이 있는데

sql injection 는 mysql 같은 db(데이터베이스) 사용하는 페이지에서 취약점을 찾아

그 사이트에 주입을 시키는것이다.

예를들어 

sql injection 으로 참이 되게 주입을 시켜

로그인을 우회하거나 admin 같은 권한유저를 탈취할 수 있다.
