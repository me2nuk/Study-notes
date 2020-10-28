# sql injection


### sql injection 이란?

> 데이터베이스를 사용하는 과정에서 의도치 않은 데이터를 주입하는것

sql는 데이터베이스의 데이터들을 관리하기위해 설계된 프로그래밍 언어이다.

자주쓰이는 sql 종류는

mysql , mssql , mongo 등등이 있는데

sql injection 는 mysql 같은 db(데이터베이스) 사용하는 페이지에서 취약점을 찾아

그 사이트에 주입을 시키는것이다.

```sql
SELECT * FROM member WHERE id='' and pw='';
```
위의 sql query 로 유저존재하는지 체크한다면

어떤 해커가 악의적으로
' or 1=1 --' 와 같은 쿼리를 넣는다면 로그인 우회가 되는 경우가있다.
```sql
SELECT * FROM member WHERE id='' or 1=1 --pw='';
```

이런식으로 pw='' 이라는 조건을 -- 같은 주석으로 예외시켜버리는것이다.

### 마무리

이처럼 sql injection 으로 인해
사람들의 정보 , 웹 권한 등이 탈취되거나 노출되어서 큰 피해를 입은 사례도있다.