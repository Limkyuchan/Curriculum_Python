class TestClass:
    def __del__(self):
        print(f'__del__({self}) 객체 소멸')

o1 = TestClass()
o2 = TestClass()
print('o1:', o1)
print('o2:', o2)
o1 = o2 # o1객체의 참조 카운트가 0이됨
print('o1:', o1)
print('o2:', o2)