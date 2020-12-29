# SQL

### SQL 이란?

SQL은 관계형 데이터베이스 관리 시스템(RDBMS)으로 
데이터를 관리하기 위해 설계된 프로그래밍 언어이다.

<br>

### SQL 문법 종류

SQL 문법 종류에는 4가지가 존재하는데 하나씩 작성해보자면 밑의 표와 일치하다.

+ DDL
+ DML
+ DCL
+ TCL

<br>

+ #### DDL

    데이터 구조를 생성, 변경, 삭제를 처리하는 데이터 정의어

    + ##### CREATE

        새로운 데이터베이스 관례 만드는 명령어

        <br>

        ```SQL
        ex) CREATE DATABASE (DATABASENAME);
        ```


    + ##### ALTER

        테이블 구조 변경할때 사용되는 명령어

        <br>

        ```SQL
        ex) ALTER TABLE (TABLE_NAME) (COMMAND) (COLUMN TYPE);
        ```

    + ##### DROP

        테이블 구조 전체 삭제할때 사용되는 명령어

        ```SQL
        ex) DROP TABLE (TABLE_NAME);

        ex) DROP DATABASE (DATABASE_NAME);
        ```

    + ##### RENAME

        테이블명을 변경할떄 사용되는 명령어

        ```SQL
        ex) ALTER TABLE (TABLE_NAME) RENAME TO (NEW TABLE_NAME);
        ```

<br>

+ #### DML

    데이터를 조회, 수정, 삭제하기위해 사용되는 언어이다.

    + ##### INSERT

        데이터 삽입하는 명령어

        ```SQL
        ex) INSERT INTO (TABLE_NAME)(COLUMN NAME) VALUES(VALUE);
        ```

    + ##### UPDATE

        데이터 수정하는 명령어

        ```SQL
        ex) UPDATE (TABLE_NAME) SET (COLUMN NAME) = (SET VALUE) WHERE (COLUMNE NAME)=(COLUMNE VALUE);
        ```

    + ##### DELETE

        데이터 삭제하는 명령어

        ```SQL
        ex) DELETE FROM (TABLE_NAME) WHERE (COLUMN_NAME)=(VALUE);
        ```

    + ##### SELECT

        데이터 조회 명령어

        ```SQL
        ex) SELECT (COLUMN NAME) FROM (TABLE_NAME);

        ex) SELECT (COLUMN NAME) FROM (TABLE_NAME) WHERE (COLUMN_NAME) = (VALUE);
        ```


+ #### DCL

    + ##### GRANT

        특정 작업 수행권한 부여 명령어

        ```SQL
        ex) GRANT (권한 종류) ON (대상) TO (USER NAME) IDENTIFIED BY (PASSWORD);
        ```

    + ##### REVOKE

        특정 권한 삭제 명령어

        ```SQL
        ex) REVOKE (권한 종류) FROM (삭제할 User)
        ```


+ #### TCL

    + ##### COMMIT

        트랜잭션 실행 작업 완료시키는 명령어

        ```SQL
        ex) COMMIT;
        ```

    + ##### ROLLBACK

        트랜잭션 실행 작업 취소시키는 명령어

        ```SQL
        ex) ROLLBACK;
        ```
