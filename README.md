# mysql (sql injection or mysql query)
<br><br><br><br>
> ( ) <- 강조 ( ) 기호는 제외

<br><br><br><br>

__Mysql Table 조회 query__
***

~~~~sql
SELECT * FROM (TABLE name);
~~~~
<br><br>

__Mysql Table 조건있는 조회 query__
***

~~~~sql
SELECT * FROM (TABLE name) where (column name) = (Condition);
~~~~
<br><br>

__Mysql Table 조건있는 조회 여러개 query__
***

~~~~sql
SELECT * FROM (TABLE name) where (column name) = (Condition) or (column name) = (Condition) and (column name) = (Condition);
or 또는 and 로 여러개 연결
~~~~