#재정의 된 메서드 호출(protected, private 개념) 의미 없음
class A:
    def _methodA(self):
        print('_methodA')
        self.__methodB()

    def __methodB(self):
        print('__methodB')

class B(A):
    def method(self):
        print('B.method()')
        self._methodA() # 부모 메서드 호출 가능(protected)
        #self.__methodB() # 부모 메서드 호출 불가(private) AttributeError

def main():
    ob = B()
    print(dir(ob))
    ob._methodA()
    ob.method()
    # ob.__methodB() # 호출 불가(private)

main()


