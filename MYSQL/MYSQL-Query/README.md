# MYSQL query
<br><br><br><br>
> ( ) <- 강조 ( ) 기호는 제외

<br><br><br><br>

__Mysql Table 조회 query__
***

~~~~sql

SELECT * FROM (TABLE name);

예) SELECT * FROM member;

~~~~
<br><br>

__Mysql Table 조건있는 조회 query__
***

~~~~sql

SELECT * FROM (TABLE name) where (column name) = (Condition);

예) SELECT * FROM member where id = 'admin';

~~~~
<br><br>

__Mysql Table 조건있는 조회 여러개 query__
***

~~~~sql

SELECT * FROM (TABLE name) where (column name) = (Condition) or (column name) = (Condition) and (column name) = (Condition);

예) SELECT * FROM member where id = 'admin' and pw = 'password';

or 또는 and 로 여러개 연결

~~~~

__Mysql Table 데이터 추가__
***

~~~~sql

INSERT INTO VALUES((원하는 데이터));

예) INSERT INTO VALUES("hello","world");

단 VALUES 만 사용하는 경우 컬럼 순서대로 데이터 추가

~~~~
<br><br>

__Mysql Table 원하는 컬럼 데이터 추가__
***

~~~~sql

INSERT INTO ((데이터 추가할 컬럼 이름 , 로 구분)) VALUES(추가할 데이터);

예) INSERT INTO (id,pw) VALUES("admin","password");

단 추가할 컬럼 이름 이상의 VALUES 를 입력할시 에러 발생

~~~~
<br><br>

__Mysql Table 원하는 컬럼 데이터 변경__
***

~~~~sql

UPDATE (TABLE name) SET (변경하고싶은 데이터) WHERE (변경할 데이터의 조건);

예) UPDATE member SET pw='password' WHERE id='admin';

WHERE 앞에있는 조건에 종촉한 데이터들 변경

~~~~
<br><br>

__Mysql Table 원하는 컬럼 데이터 삭제__
***

~~~~sql

DELETE FROM (TABLE name) WHERE (데이터 삭제할 컬럼 이름) = (삭제할 데이터);

예) DELETE FROM member WHERE id='admin';

WHERE 앞에있는 조건들의 열이 제거된다.

~~~~
<br><br>
