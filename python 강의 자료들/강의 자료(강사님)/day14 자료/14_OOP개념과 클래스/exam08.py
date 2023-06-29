class Person:
    dept = ''

    def __init__(self):
        print(self,'객체 생성')

    def setInfo(self, name, age):
        self.name = name
        self.age = age
    
    def printInfo(self):
        print('printInfo()를 호출한 객체:', self)
        print(Person.dept, self.name, self.age)

Person.dept = '영업부'

p1 = Person()
p1.setInfo('원빈', 40)

p2 = Person()
p2.setInfo('강동원', 30)
print('p1:', p1)
p1.printInfo()
print('p2:', p2)
p2.printInfo()