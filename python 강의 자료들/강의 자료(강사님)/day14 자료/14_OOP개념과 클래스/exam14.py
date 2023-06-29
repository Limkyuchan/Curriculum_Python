class Person:
    def __init__(self, name = None, age = 0):
        self.__name = name
        self.__age = age

    def printInfo(self):
        print(self.__name, self.__age)

def main():
    p1 = Person('홍길동', 20)
    print(p1.__dict__)
    print(dir(p1))
    p1.__dict__['age'] = 30 # age가 추가됨
    p1.__dict__['__age'] = 40 # __age가 추가됨
    print(p1.__age) # 객체의 __age가 아닌 추가된 멤버 __age에 접근
    #만약 __age를 추가하지 않았다면 AttributeError 발생
    p1.printInfo()
    print(p1.age) # 추가된 age
    print(dir(p1))

main()


