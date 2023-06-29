class Person:
    def __init__(self, name='', age=0):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f'Person[name={self.name}, age={self.age}]'

#Person객체 사용하기
p1 = Person()
print(p1)
p1.name = '이순신'
p1.age = 32
p2 = Person('홍길동', 20)
print(p1)
print(p2)
print()

class PersonManager:
    def __init__(self, size = 5):
        self.size = size
        self.pl = {}
        self.no = 0
    
    def insert(self, ps):
        if len(self.pl) == self.size:
            return
        if isinstance(ps, Person):
            self.pl.__setitem__(self.no, ps)
            self.no += 1
    
    def select(self, no):
        return self.pl.get(no)

    def sorted(self):
        return sorted(self.pl.items(), key=lambda x:x[1].age, reverse=True)

#Person 타입의 객체를 관리하는 클래스 사용 예시
pm = PersonManager(10)

pm.insert(Person('이순신', 20))
pm.insert(Person('홍길동', 30))
pm.insert(Person('임꺽정', 15))
pm.insert(Person('김좌진', 33))
pm.insert(Person('장보고', 27))
pm.insert(Person('김구', 10))

for no in range(0, 10):
    if no != None:
        print(pm.select(no))

print()

for ps in pm.sorted():
    print(ps[1])