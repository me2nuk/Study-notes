# MYSQL query
<br>
> ( ) <- 강조 ( ) 기호는 제외

<br><br>

__MySQL DATABASE 조회 query__
***

~~~~sql
SHOW DATABASES;
~~~~
<br><br>

__MySQL Table 조회 query__
***

~~~~sql
SHOW TABLES;
~~~~
<br><br>


__MySQL DATABASE 생성 query__
***

~~~~sql

CREATE DATABASE (DATABASE name);

ex) CREATE DATABASE databasename;

~~~~
<br><br>


__MySQL Table 데이터 조회 query__
***

~~~~sql

SELECT * FROM (TABLE name);

ex) SELECT * FROM member;

~~~~
<br><br>

__MySQL Table 데이터 조건있는 조회 query__
***

~~~~sql

SELECT * FROM (TABLE name) where (column name) = (Condition);

ex) SELECT * FROM member where id = 'admin';

~~~~
<br><br>

__MySQL Table 데이터 여러 조건 조회 query__
***

~~~~sql

SELECT * FROM (TABLE name) where (column name) = (Condition) or (column name) = (Condition) and (column name) = (Condition);

ex) SELECT * FROM member where id = 'admin' and pw = 'password';

or 또는 and 로 여러개 연결

~~~~

<br><br>

__MySQL Table 데이터 추가__
***

~~~~sql

INSERT INTO VALUES((원하는 데이터));

ex) INSERT INTO VALUES("hello","world");

단 VALUES 만 사용하는 경우 컬럼 순서대로 데이터 추가

~~~~
<br><br>

__MySQL Table 원하는 컬럼 데이터 추가__
***

~~~~sql

INSERT INTO ((데이터 추가할 컬럼 이름 , 로 구분)) VALUES(추가할 데이터);

ex) INSERT INTO (id,pw) VALUES("admin","password");

단 추가할 컬럼 이름 이상의 VALUES 를 입력할시 에러 발생

~~~~
<br><br>

__MySQL Table 원하는 컬럼 데이터 변경__
***

~~~~sql

UPDATE (TABLE name) SET (변경하고싶은 데이터) WHERE (변경할 데이터의 조건);

ex) UPDATE member SET pw='password' WHERE id='admin';

WHERE 앞에있는 조건에 종촉한 데이터들 변경

~~~~
<br><br>

__MySQL Table 원하는 컬럼 데이터 삭제__
***

~~~~sql

DELETE FROM (TABLE name) WHERE (데이터 삭제할 컬럼 이름) = (삭제할 데이터);

ex) DELETE FROM member WHERE id='admin';

WHERE 앞에있는 조건들의 열이 제거된다.

~~~~
<br><br>
