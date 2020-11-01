def hello():
    print('helloworld')
hello()

def factor(variable):
    print(variable)
factor('helloworld')

def function(hello = 'hello'):
    print(hello)

function('world')
function()

def ListVariable(hello = []):
    print(hello)

ListVariable([1,2,3,4])
ListVariable()

def ListVariable(hello = []):
    print(hello)
    print(type(hello))

ListVariable()

def SpecialVariable(*args, **keywords):

    for argsVariable in args:
        print(argsVariable)
    for key in keywords:
        print(key," -> ",keywords[key])
    print(type(args))
    print(type(keywords))
    print(args)
    print(keywords)

SpecialVariable('a','b','c',a = 'a',b = 'b',c = 'c')

def one( a , / ):
    print(a)
    print(type(a))

try:
    one('1')
    one(a = '1')

except Exception as ex:
    print(ex,end='\n\n')

def one( * , a ):
    print(a)
    print(type(a))

try:
    one('1')
    one(a = '1')

except Exception as ex:
    print(ex,end='\n\n')

def ReturnFunc(sum_one , sum_two):
    num = sum_one + sum_two
    return num

result = ReturnFunc(20,5)
print(result)
print(ReturnFunc(20,5))

def ReturnFunc(sum_one , sum_two):
    return sum_one + sum_two

result = ReturnFunc(20,5)
print(result)
print(ReturnFunc(20,5))