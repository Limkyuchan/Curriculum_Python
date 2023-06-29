class Person:
    def __init__(self, name = None, age = 0):
        self._name = name
        self._age = age

    def printInfo(self):
        print(self._name, self._age)

def main():
    p1 = Person('홍길동', 20)
    print(p1.__dict__)
    print(dir(p1))
    p1.__dict__['age'] = 30 # age가 추가됨
    p1.__dict__['_age'] = 40 # _age가 변경됨
    print(p1._age) # 변경된 _age 출력됨
    p1.printInfo()
    print(p1.age) # 추가된 age
    print(dir(p1))

main()

