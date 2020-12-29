# blind sql injection

#### node.js

node.js 로 blind sql injection 
구현하기

<br>
 
node.js 은 구현하면 저렇게 되지만 

자세한 blind sql injection query는 밑의 링크 참고

[blind sql injection python script](https://github.com/kimminwyk/Study-notes/blob/master/SQL/MYSQL/MYSQL-SQL-injection/blind-sql-injection/blind-sql-injection-python-script.md "python script")


### request module

```js
const request = require('request');

const Webrequest = function(url, data = null, headers = null, methodCheck = 'get') {

    if (methodCheck == 'get') {
        request.get({ url: url, headers: headers }, function(err, response, body) {
            if (err) console.log('err');

            console.log(body);
        });
    } else if (methodCheck == 'post') {
        request.post({ url: url, form: data, headers: headers }, function(err, response, body) {
            if (err) console.log('err');

            console.log(body);
        });
    }
}
for(var i = 0; i < 10; i++){
    Webrequest('https://www.google.com', methodCheck = 'post');
}
```

### axios module

```js
const axios = require('axios');

const Webrequest = function(url, methodCheck = 'get', params = null, headers = null, data = null) {
    if (methodCheck == 'get') {

        axios.get(url, { params: params })
            .then(res => {
                console.log(res.data);
            });
    } else if (methodCheck == 'post') {
        axios.post(url, { data: data, headers: headers })
            .then(res => {
                console.log(res.data);
            })
    }
}

for (var j = 0; j < 1; j++) {
    Webrequest(url = 'https://www.google.com', methodCheck = 'post');
}
```


이런식으로 간단하게 request, axios module를 이용해서 post 또는 get 방식으로 통신할수있게 만들었다.

만약에 여러번 반복해서 요청하고싶다면

```js
for (var j = 0; j < 10; j++) {
    Webrequest('https://www.google.com', methodCheck = 'post');
}
```

이런식으로 반복문을 이용해서 할수있다.

만약에 login 같은 무언가를 감지하고싶다면 Webrequest 함수를 응용하여 if 같이 조건문을 사용한다면 

제대로 사용할 수 있다.

### 마무리

node.js 랑 python 이랑 문법과 속도적인면에서 차이는 나지만

blind sql injection 전송하는 쿼리 방식은 크게 다르지 않다.

node.js 는 속도가 빨라서 사용할 줄만 안다면 천상의 속도를 느낄 수 있다.

![gooooooooo image](./image/goooooo.jpg)