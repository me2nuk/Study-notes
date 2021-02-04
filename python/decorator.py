def decorators(Function):
    print(Function.__name__)
    Function()
    
@decorators
def index():
    print('decorators Function')

def decorators1(args):
    def _args(Function):
        print(args)
        print(Function.__name__)
        Function()
        print(Function)
    return _args

@decorators1(2)
def index1():
    print('hello')

def decorators2(_sum):
    def add(Function):
        print(_sum + Function())

    return add

@decorators2(10)
def index2():
    return 10


class ClassDecorator:
    def __init__(self, Function):
        print(Function)
        print(Function.__name__)
        print(Function())
    
@ClassDecorator
def ClassIndex():
    print('hello')
    return 'hello'