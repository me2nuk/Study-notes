# node.js request

### request module

```js

var request = require('request');

const sqli = function blindsqli(Blind){
	request.get({url:'https://google.com?id='+Blind},function(err,response,body){
		if(body.indexOf('Login Clear!') != -1){
		    console.log('Blind sql injection Result length :',i);
		}
	});
}

for(var length = 0; length < 10; length++){
		setTimeout(sqli,i,length);
}

```

위의 코드같은경우 request module 를 사용하여 

setTimeout 함수로 length 값을 인자로 넘겨 요청한 웹을 스크래핑후

indexOf 로 자신이 원하는 문자열을 찾은다음 console.log 로 출력

하지만 node.js 에는 request 모듈 말고도 axios 를 사용할있다.

만약에 자신이 get 가 아닌 post 로 body 를 넘겨야될 결우 form:{'data key name':'data key name in value'}

이런식으로 get({})안에 넣어서 전송하면은 된다.