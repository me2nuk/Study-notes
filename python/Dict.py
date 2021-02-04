a = {
    'a':'c',
}
print(a)

a = {
    'a':'c'
}
print(a)
print(a.items())

for key,value in a.items():
    print(key,value)

print(a.values())
print(a.keys())

Dict = {
    'Keys1':'Values1',
    'Keys2':'Values2',
    'Keys3':'Values3'
}

for key, value in a.items():
    print(key)
    print(value)

for keys in a.keys():
    print(keys)

for values in a.values():
    print(values)

GetDict = {
    'test1':'testname',
    'name':'kmw',
    'foo':'bar'
}

print(GetDict.get('test1'))
print(GetDict.get('name'))

print(GetDict['test1'])
print(GetDict['name'])

GetDict.update({'name2':'kim'})
print(GetDict['name2'])
GetDict.update(name='mmm')
print(GetDict['name'])

print(GetDict.pop('name2'))
print(GetDict)
print(GetDict.pop('name'))
print(GetDict)
print(GetDict.pop('ffff','No ffff keys'))
print(GetDict)

a = GetDict.copy()
print(f"a : {a}")

print(f'popitem one : {GetDict.popitem()}')
print(GetDict)
print(f'popitem two : {GetDict.popitem()}')
print(GetDict)

print(dict.fromkeys('hello'))
test = ['t','e','s','t']
print(dict.fromkeys(test))

print(a)
print(a.setdefault('set'))
print(a)
print(a.setdefault('set_1','setdefaultvalue'))
print(a)

print(a.clear())
print(a)