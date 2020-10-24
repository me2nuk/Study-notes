# blind sql injection

#### node.js

node.js 로 blind sql injection 
구현하기

[python_script](https://github.com/kimminwyk/Study-notes/tree/master/MYSQL/MYSQL-SQL%20injection/blind-sql-injection/blind-sql-injection-python-script.md "python script")


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

Webrequest('https://www.google.com', methodCheck = 'post');
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
    Webrequest(url = 'https://nebori.tistory.com/13', methodCheck = 'post');
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