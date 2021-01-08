# function

## <div id="def">def</div>

def 라는 키워드는 함수를 정의할 때 시작합니다.
### 함수 정의하기

```py
>>> def hello():
...     print('helloworld')
...
>>> hello()
helloworld
```

위의 코드는 def 키워드로 hello 라는 함수를 정의하며
해당 hello 함수에 print 함수로 helloworld 를 출력하게 만들어져있고

hello() 함수를 호출 시 helloworld를 출력한다.

### 함수 인자 받기

```py
>>> def factorial(variable):
...     print(variable)
...
>>> factorial('helloworld')
helloworld
```

factorial 함수를 정의하면서 variable이라는 매개변수로 인자를 받아

vriable 변수를 출력한다.

### 기본 인자 값

```py
>>> def factorial(hello = 'hello'):
...     print(hello)
...
>>> factorial('world')
world
>>> factorial()
hello
```

factorial 이라는 함수에 hello이란 매개변수의 기본값이 'hello'로 정의되어있기 때문에

hello 변수에 인자를 안 넣어도 hello 가 출력된다.

```py
>>> def ListVariable(hello = []):
...     print(hello)
...
>>> ListVariable([1,2,3,4])
[1, 2, 3, 4]
>>> ListVariable()
[]
>>> def ListVariable(hello = []):
...     print(hello)
...     print(type(hello))
...
>>> ListVariable()
[]
<class 'list'>
```

위의 코드는 ListVariable 함수에 hello 매개변수를 list 형으로 기본값을 정의하고

밑의 함수를 다시 재정의하고 type(hello)를 추가했더니

기본값으로 list 타입으로 되어있는 것을 볼 수 있다.

### 특수 매개변수

```py
>>> def SpecialVariable(*args, **keywords):
...     for argsVariable in args:
...             print(argsVariable)
...     for key in keywords:
...             print(key," -> ",keywords[key])
...     print(type(args))
...     print(type(keywords))
...     print(args)
...     print(keywords)
...
>>> SpecialVariable('a','b','c',a = 'a',b = 'b',c = 'c')
a
b
c
a  ->  a
b  ->  b
c  ->  c
<class 'tuple'>
<class 'dict'>
('a', 'b', 'c')
{'a': 'a', 'b': 'b', 'c': 'c'}
```

*args 는 tuple 형이고
**keywords는 dict 형으로 기본 정의된다.

'a','b','c' 는 *args 변수에 들어가고
a = 'a' , b = 'b' , c = 'c' 는 **keywords 변수게 들어가게 된다.

전달되는 방식을 이미지로 본다면

<br>

![def function image](./image/dict_tuple.png)


이런 식으로 전달된다.

### 특수 매개 변수

특수 키워드로 인자 전달될 때 방법을 제한하여 가동성과 성능을 늘릴 수 있습니다.

#### / keyword 제한

```py
>>> def one( a , / ):
...     print(a)
...     print(type(a))
...
>>> one('1')
1
<class 'str'>
>>> one(a = '1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: one() got some positional-only arguments passed as keyword arguments: 'a'
```

one 함수에서 매개변수 a에 keywords 제한을 두고 정의했다.

인자를 전달할 때 Positional(위치)로 값을 전달하여야 한다.

one('1')에서 a의 위치에 '1' 변수를 전달하고

one(a = '1')에서는 keywords 형식으로 '1'을 전달하더니 

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: one() got some positional-only arguments passed as keyword arguments: 'a'
```

위와 같이 에러가 나는 것을 확인할 수 가 있다.

에러가 나지않고 올바을 형식으로 인자로 전달하기위해서 Postitional 위치로 전달해야된다.

그리고 인자 생성할 때 
```py
def <원하는 변수 이름>(<원하는 인자 이름>, / ):
```

이런식으로 하면 된다.

#### * Positional 제한

```py
>>> def one( * , a ):
...     print(a)
...     print(type(a))
...
>>> one('1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: one() takes 0 positional arguments but 1 was given
>>> one(a = '1')
1
<class 'str'>
```

새로 one 함수 정의할때 a 매개변수를 Positional 제한시켰다.

이처럼 a 변수에 위치로 전달하는것이 아닌

keyword 형식으로 

one(a = '1') 같이 전달해야된다.

그래서 one('1') 이렇게 전달하면 

```py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: one() takes 0 positional arguments but 1 was given
```

이렇게 에러가 발생하는 것을 볼 수 가있다.

### return 리턴

__return 은 정의한 함수에서 반환하는 값이라고 생각하면 된다.__

```py
def <원하는 함수 이름>(<받을 인자>):
    <코드 처리>
    return <반환하고싶은 변수 또는 값>
```

위처럼 정의하면은 된다.

```py
>>> def ReturnFunc(sum_one , sum_two):
...     num = sum_one + sum_two
...     return num
...
>>> result = ReturnFunc(20,5)
>>> print(result)
25
>>> print(ReturnFunc(20,5))
25
```

ReturnFunc 함수는 인자 1 과 인자 2 를 받아

합을 한 값을 리턴한다.

```py
result = ReturnFunc(20,5)
```

아니면

```py
print(ReturnFunc(20,5))
```

이렇게 정의해도 무방하다.

그리고 return하는 과정에서 연산을 해도 상관없다.

위의 코드를 최적화 시킨다면

```py
def ReturnFunc(sum_one , sum_two):
    return sum_one + sum_two
```

이런식으로 선언하면 가독성이 좋아직호 코드가 좀 더 최적화 된다.

```py
>>> def ReturnFunc(sum_one , sum_two):
...     return sum_one + sum_two
...
>>> result = ReturnFunc(20,5)
>>> print(result)
25
>>> print(ReturnFunc(20,5))
25
```

전 코드처럼 함수를 호출해도 기능은 똑같다.

## <div id="lambda">lambda</div>

lambda 표현식

lambda는 def 키워드를 사용하는 일반적인 함수 정의가 아닌 익명 함수이다.

def를 이용한 함수와는 다르게 한줄로만 가능하며 일방적으로 여러줄로는 불가능하다.

예를 들어 def 키워드를 이용하여 인자를 넣고 100을 더한 값을 반환하는 함수를 만들면

```py
>>> def Function(x):
...     return x + 100
...
>>> Function(100)
200
```

이런식으로 정의하여 Function 이라는 함수를 만들 수 있다.

하지만 lambda 를 이용하면

```py
>>> Function = lambda x : x + 100
>>> Function(100)
200
```

이런식으로 사용될 수 있다.
Function 이라는 변수에
lambda 로 만든 익명 함수에 x 인자를 받아 x+100 가 반환되게 한것이다.

하지만 lambda는 def 과는 다르게 return 를 사용하지 않으며
```py
lambda 인자 : 결과
```
의 결과 부분을 자동으로 반환하게된다.

다음과 같이 Function 변수에 할당하지 않아도 다른 방법으로는

변수에 할당하여 지속적으로 사용하는것과 일시적으로 생성하여 사용하는 방법이있다.

```py
>>> sum = lambda x, y : x+y # x y 2개의 인자 받고 더함
>>> sum(24,52)
76
>>> (lambda x,y : x+y)(24,52)# 일시적으로 생성한 후 익명 함수 생성
76
```

이처럼 sum 변수에 할당한것과 ()() 형식으로 일시적으로 만든것과 코드는 다르지만 

결과 부분에서는 일치하다.

그리고 lambda를 좀더 효율적으로 사용하기 위해서는 다양한 방법이 존재한다. 

```py
>>> (lambda *args : args)('a','b','c','d')
('a', 'b', 'c', 'd')
>>>
>>>
>>> (lambda **keywords : keywords)(a = 'test a',b = 'test b',c = 'test c',d = 'test d')
{'a': 'test a', 'b': 'test b', 'c': 'test c', 'd': 'test d'}
>>>
>>>
>>> (lambda * , a : a)(a = 'a')
'a'
>>>
>>>
>>> (lambda * , a : a)('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() takes 0 positional arguments but 1 was given
>>>
>>>
>>> (lambda  a , / : a)('a')
'a'
>>>
>>>
>>> (lambda  a , / : a)(a = 'a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() got some positional-only arguments passed as keyword arguments: 'a'
>>>
```

이렇게 일부 기능인 Positional keyword , *args , **keywords 등 다양한 기능이 사용 가능하다.

그리고 람다 함수를 이용하여 문제를 한번 풀어볼것이다.

<br>

> 1. n 을 인자로받아 n만큼 반복하면서 리스트를 만들고 해당 리스트 요소의 합을 구하시오

리스트 예시 
__input__ : 5
__output [1,2,3,4,5]__ : 15

* * *

> 2. n 을 입력받아 n만큼 반복하여 n단까지 구구단을 출력한다

__input__ : 5
__output__ :
1 * 1 = 1
1 * 2 = 2
...
5 * 9 = 45

<br>

##### 1번 문제

```py
>>> print(sum((lambda x : [i for i in range(0,int(x))])(input())))
5
10
```

<br>

##### 2번 문제

```py
>>> print('\n'.join((lambda x : [f"{i} * {j} = {i*j}" for i in range(1, x+1) for j in range(1,10)])(int(input()))))
5
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
...
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
```

<br>

이런식으로 람다 표현식을 이용하여 구구단과 리스트 합을 한줄로 쉽게 만들었다.

생각보다 복잡해보일수도있겠지만 
큰 기능이 아닌 일시적으로 작은 기능을 사용할려고 할때 자주쓰일것 같다.

### 마무리

python 공식 자료 링크

[python notice link](https://docs.python.org/ko/3/tutorial/controlflow.html#defining-functions)
