class Person:
    dept = 'Unknown'
    def setInfo(self, name, age):
        print('setInfo()를 호출한 객체:', self)
        self.name = name
        self.age = age
    def printInfo(self):
        print('printInfo()를 호출한 객체:', self)
        print(Person.dept, self.dept, self.name, self.age)

Person.dept = '영업부' #클래스 범위에 속하는 변수

p1 = Person()
p1.setInfo('원빈', 40)

p2 = Person()
p2.setInfo('강동원', 30)

p1.printInfo()
p2.printInfo()

print('p1객체 참조 값:', p1)
print('p2객체 참조 값:', p2)