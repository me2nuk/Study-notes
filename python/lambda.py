_lambda1 = lambda x : x + x
#lambda Function return (x+x)

print(_lambda1(1), _lambda1(20))

_lambda2 = lambda x, y : x + y
#lambda Function return (x+y)

print(_lambda2(1,5), _lambda2(5,3))

_lambda3 = lambda x : sum([i for i in range(int(x))])
#lambda Function return (sum([i for i in range(int(x))]))

print(_lambda3(5), _lambda3(10))

_lambda4 = lambda x = 1 : x
#lambda Function return (x)

print(_lambda4(), _lambda4(5))

_lambda5 = lambda *args, **kwargs : (args,kwargs)
#lambda Function return ((args, kwargs))

print(_lambda5('a', 'b', 'c', a = 'a', b = 'b', c = 'c'))

_lambda6 = lambda positions, / : positions
#lambda Function return positions / keywords 제한

print(_lambda6('1'))

try:
    print(_lambda6(positions = '1'))
    #Error
except:
    print('lambda keywords 제한')

_lambda7 = lambda *, keywords : keywords
#lambda Function return keywords / positions 제한

print(_lambda7(keywords = '1'))

try:
    print(_lambda7('1'))
    #Error
except:
    print('lambda positions 제한')
