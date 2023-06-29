class TestClass:
    def __init__(self, n = None): # 인자의 타입을 이용하여 생성자 오버로딩 개념 적용
        print('생성자에 전달된 값 타입:', type(n))
        self.value = n

        if n == None:
            self.printNone()
        elif type(n) == int:
            self.printInt()
        elif type(n) == float:
            self.printFloat()
        elif type(n) == str:
            self.printStr()
    
    def printInt(self):
        print('int:', self.value)
    def printFloat(self):
        print('float:', self.value)
    def printStr(self):
        print('str:', self.value)
    def printNone(self):
        print('None:', self.value)

class Person:
    dept = ''

    def __init__(self, *args): # 가변 인자를 이용한 생성자 오버로딩 개념 적용
        argssize = len(args)
        self.name = None
        self.age = 0
        if argssize == 1:
            self.name = args[0]
        elif argssize == 2:
            self.name = args[0]
            self.age = args[1]    

    def setInfo(self, name, age):
        self.name = name
        self.age = age
    
    def printInfo(self):
        print('printInfo()를 호출한 객체:', self)
        print(Person.dept, self.name, self.age)

Person.dept = '영업부'
p0 = Person()
p1 = Person('원빈')
p2 = Person('강동원', 30)

p0.printInfo()
p1.printInfo()
p2.printInfo()
print()

o1 = TestClass(1)
o2 = TestClass(3.14)
o3 = TestClass('hello')
o4 = TestClass()
