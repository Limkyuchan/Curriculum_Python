class Person:
    dept = ''
    def setInfo(self, name, age):
        self.name = name
        self.age = age
    
    def printInfo(self):
        print(self.dept, self.name, self.age)

Person.dept = '영업부'

p1 = Person()
p1.setInfo('원빈', 40)

p2 = Person()
p2.setInfo('강동원', 30)

p1.printInfo()
p2.printInfo()

print()
p2.dept = '기술부'
Person.deptno = 12 # 클래스 변수 추가 
p1.printInfo()
p2.printInfo()

print()
print(p1.dept)
print(p2.dept)
print(Person.dept)
print(Person.deptno)
print(p1.deptno)
print(p2.deptno)

