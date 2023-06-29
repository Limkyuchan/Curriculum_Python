class Person:
    dept = ''

    def setInfo(self, name, age):
        self.name = name
        self.age = age
    
    def printInfo(self):
        print(Person.dept, self.name, self.age)

    @classmethod
    def deptPrint(cls):
        # self.name = '' # 인스턴스 멤버 접근 불가
        print(cls.dept)

    @staticmethod
    def personInit(ps):
        Person.dept = 0
        ps.name = None
        ps.age = 0

Person.dept = '영업부'

p1 = Person()
p1.setInfo('원빈', 40)

p2 = Person()
p2.setInfo('강동원', 30)

p1.printInfo()
p2.printInfo()

print()
p1.deptPrint()
p2.deptPrint()
Person.dept = '개발부'
p1.deptPrint()
p2.deptPrint()
print()

p1.printInfo()
p2.printInfo()
Person.personInit(p1) # 객체참조가 아닌 클래스명으로 호출!
p1.printInfo()
p2.printInfo()
Person.personInit(p2)
p1.printInfo()
p2.printInfo()


