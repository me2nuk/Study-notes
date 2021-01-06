class PythonClassMetHodList:

    def __init__(self) -> None:
        self.ListVariable = [1,2,3,4,5]
        self.SlefNumber = 30
        self.DelVariable = 'Hello World'

    def __len__(self):
        """
        len 함수가 호출될때에 실행되는 메소드
        """
        return len(self.ListVariable)

    def __del__(self):
        """
        클래에 의해 만들어진 객체가 소멸될때 호출되는 메소드
        """
        del self.DelVariable

    def __getitem__(self, position):
        """
        sum 함수가 호출될때에 실행되는 메소드
        """
        print(f'반복 수 : {position}')
        return self.ListVariable[position]
    
    def __contains__(self, position):
        """
        in 키워드에 사용될때 실행되는 메소드
        """
        return self.ListVariable

    ####################################################
    """단순 연산자"""
    def __add__(self, Number):
        print(f'+ 연산자 호출 : {Number}')
        return self.SlefNumber + Number
    
    def __sub__(self, Number):
        print(f'- 연산자 호출 : {Number}')
        return self.SlefNumber - Number

    def __mul__(self, Number):
        print(f'* 연산자 호출 : {Number}')
        return self.SlefNumber * Number

    def __pow__(self, Number : list):
        print(f'** 연산자 호출 : {Number}')
        return self.SlefNumber ** Number

    def __div__(self, Number):
        print(f'/ 연산자 호출 : {Number}')
        return self.SlefNumber / Number

    def __floordiv__(self, Number):
        print(f'// 연산자 호출 : {Number}')
        return self.SlefNumber // Number
    
    def __mod__(self, Number):
        print(f'% 연산자 호출 : {Number}')
        return self.SlefNumber % Number

    def __lshift__(self, Number):
        print(f'>> 연산자 호출 {Number}')
        return self.SlefNumber >> Number
        
    def __rshift__(self, Number):
        print(f'<< 연산자 호출 {Number}')
        return self.SlefNumber << Number
    
    def __and__(self, Number):
        print(f'& 연산자 호출 {Number}')
        return self.SlefNumber & Number
    
    def __xor__(self, Number):
        print(f'^ 연산자 호출 {Number}')
        return self.SlefNumber ^ Number

    def __or__(self, Number):
        print(f'| 연산자 호출 {Number}')
        return self.SlefNumber | Number

    ####################################################
    """역순 산술 연산자"""

    def __radd__(self, Number):
        print('Right + 연산자 호출')
        return Number + self.SlefNumber

    def __rsub__(self, Number):
        print('Right - 연산자 호출')
        return Number - self.SlefNumber

    def __rmul__(self, Number):
        print('Right * 연산자 호출')
        return Number * self.SlefNumber

    def __rtruediv__(self, Number):
        print('Right / 연산자 호출')
        return Number / self.SlefNumber

    def __rfloordiv__(self, Number):
        print('Right // 연산자 호출')
        return Number // self.SlefNumber

    def __rmod__(self, Number):
        print('Right % 연산자 호출')
        return Number % self.SlefNumber

    def __rdivmod__(self, Number):
        print('Right divmod 함수 호출')
        return divmod(Number, self.SlefNumber)

    def __rpow__(self, Number):
        print('Right ** 연산자 호출')
        return Number ** self.SlefNumber

    def __rlshift__(self, Number):
        print('Right << 연산자 호출')
        return Number << self.SlefNumber

    def __rrshift__(self, Number):
        print('Right >> 연산자 호출')
        return Number >> self.SlefNumber

    def __rand__(self, Number):
        print('Right & 연산자 호출')
        return Number & self.SlefNumber

    def __ror__(self, Number):
        print('Right | 연산자 호출')
        return Number | self.SlefNumber

    def __rxor__(self, Number):
        print('Right ^ 연산자 호출')
        return Number ^ self.SlefNumber

    ####################################################
    """복합 대입 연산자"""
    def __iadd__(self, Number):
        print(f'+= 연산자 호출 {Number}')
        awhileSlefNumber = self.SlefNumber
        awhileSlefNumber += Number
        return awhileSlefNumber

    def __isub__(self, Number):
        print(f'-= 연산자 호출 {Number}')
        awhileSlefNumber = self.SlefNumber
        awhileSlefNumber -= Number
        return awhileSlefNumber

    def __imul__(self, Number):
        print(f'*= 연산자 호출 {Number}')
        awhileSlefNumber = self.SlefNumber
        awhileSlefNumber *= Number
        return awhileSlefNumber
    
    def __ipow__(self, Number):
        print(f'**= 연산자 호출 {Number}')
        awhileSlefNumber = self.SlefNumber
        awhileSlefNumber **= Number
        return awhileSlefNumber

    def __idiv__(self, Number):
        print(f'/= 연산자 호출 {Number}')
        awhileSlefNumber = self.SlefNumber
        awhileSlefNumber /= Number
        return awhileSlefNumber

    def __ifloordiv__(self, Number):
        print(f'//= 연산자 호출 {Number}')
        awhileSlefNumber = self.SlefNumber
        awhileSlefNumber //= Number
        return awhileSlefNumber

    def __imod__(self, Number):
        print(f'%= 연산자 호출 {Number}')
        awhileSlefNumber = self.SlefNumber
        awhileSlefNumber %= Number
        return awhileSlefNumber

    def __ilshift__(self, Number):
        print(f'<<= 연산자 호출 {Number}')
        awhileSlefNumber = self.SlefNumber
        awhileSlefNumber <<= Number
        return awhileSlefNumber
    
    def __irshift__(self, Number):
        print(f'>>= 연산자 호출 {Number}')
        awhileSlefNumber = self.SlefNumber
        awhileSlefNumber >>= Number
        return awhileSlefNumber

    def __iand__(self, Number):
        print(f'&= 연산자 호출 {Number}')
        awhileSlefNumber = self.SlefNumber
        awhileSlefNumber &= Number
        return awhileSlefNumber

    def __ixor__(self, Number):
        print(f'&= 연산자 호출 {Number}')
        awhileSlefNumber = self.SlefNumber
        awhileSlefNumber ^= Number
        return awhileSlefNumber

    def __ior__(self, Number):
        print(f'&= 연산자 호출 {Number}')
        awhileSlefNumber = self.SlefNumber
        awhileSlefNumber |= Number
        return awhileSlefNumber
    
    ####################################################
    """비교 연산자"""

    def __lt__(self, ComparisonNumber):
        return self.SlefNumber < ComparisonNumber

    def __gt__(self, ComparisonNumber):
        return self.SlefNumber > ComparisonNumber

    def __le__(self, ComparisonNumber):
        return self.SlefNumber <= ComparisonNumber

    def __ge__(self, ComparisonNumber):
        return self.SlefNumber >= ComparisonNumber

    def __eq__(self, ComparisonNumber):
        return self.SlefNumber == ComparisonNumber

    def __ne__(self, ComparisonNumber):
        return self.SlefNumber != ComparisonNumber

    ####################################################
    """단한 연산자"""

    def __neg__(self):
        return -self.SlefNumber

    def __pos__(self):
        return +self.SlefNumber

    def __abs__(self):
        return abs(self.SlefNumber)

    def __invert__(self):
        return ~self.SlefNumber
    
    def __complex__(self):
        return complex(self.SlefNumber)
    
    def __int__(self):
        return int(self.SlefNumber)

    def __float__(self):
        return float(self.SlefNumber)

    def __oct__(self):
        return oct(self.SlefNumber)
    
    def __hex__(self):
        return hex(self.SlefNumber)

def arg(*args):
    return args

def kwds(**keywords):
    return keywords

print(arg('HelloWorld'))
print(kwds(variable = 'HelloWorld'))
