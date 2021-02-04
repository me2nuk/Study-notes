def Function():
    return 'a'
#def Function return 'a'
print(Function())
print(Function.__name__)

def Function1(a):
    return a
#def Function1 return a

print(Function1(2), Function1('hello'))

def Function2(a, b):
    return (a,b)
#def Function2 return (a,b)

print(Function2(1,2), Function2('a',2))

def Function3(a = 5):
    return a
#def Function3 return a

print(Function3(), Function3(1))

def Function4(a = 10, b = 40):
    return (a,b)
#def Function4 return (a,b)

print(Function4(), Function4(1,2), Function4(1))

def Function5(a, /):
    return a
#def Function5 a

print(Function5(1))

try:
    print(Function5(a = 1))
except:
    print('Funection5 positions 제한')

def Function6(*, a):
    return a
#def Function6 a

print(Function6(a = '1'))

try:
    print(Function6(1))
except:
    print('Function6 keywors 제한')

def Function7(a) -> None:
    return a
#def Function7 a
print(Function7(1))
print(Function7.__annotations__)

def Function8(a : str, b :int = 5) -> str:
    return (a,b)

print(Function8(1,2), Function8(2))
print(Function8.__annotations__)

#def Function8 return (a,b)

def Function9(*args, **keywords):
    return (args, keywords)
#def Function9 return (args,keywords)

print(Function9('a','b','c',a='a',b='b',c='c'))

def Function10():
    print('helloworld')
    print('Call Function10')

Function10()
print(Function10())
#def Function10 return None