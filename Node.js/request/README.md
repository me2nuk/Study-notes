# node.js request

### request module

request module는 웹 사이트를 스크래핑 또는 크롤링을 사용하기위해 자주 쓰이는 모듈중 하나이다.

이 모듈을 이용해 원하는 사이트에 데이터를 주고받고

해당 사이트에 요청을 보낸다면 그 사이트의 소스코드를 가져올 수 있다.


## Method GET

```js

var request = require('request');

const Webrequest = function res(){
	request.get({
		url:'https://google.com',
		headers: headers
		qs: parmas
	},function(err,response,body){
		console.log(body);
	});
}

Webrequest();

```

## Method POST

```js

var request = require('request');

const Webrequest = function res(){
	request.post({
		url:'https://google.com',
		headers: headers,
		form: data
	},function(err,response,body){
		console.log(body);
	});
}

Webrequest();

```