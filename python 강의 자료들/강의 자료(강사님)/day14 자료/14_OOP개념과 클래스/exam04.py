class Person:
    dept = ''

    def setInfo(self, name, age):
        self.name = name
        self.age = age
    
    def printInfo(self):
        print(Person.dept, self.name, self.age)

print(Person.dept)
Person.dept = '영업부'
print(Person.dept)

p1 = Person()
p1.setInfo('원빈', 40)

p2 = Person()
p2.setInfo('강동원', 30)

p1.printInfo()
p2.printInfo()
print()
Person.dept = '인사부'
p1.printInfo()
p2.printInfo()

print(dir(p1))
