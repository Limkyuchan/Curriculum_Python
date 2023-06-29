#__이 적용된 메서드는 재정의가 아닌 새로 추가되는 것
class A:
    def _methodA(self):
        print('_methodA')
        self.__methodB()

    def __methodB(self):
        print('__methodB')

class B(A):
    def __methodB(self): # 재정의가 아닌 B클래스에 추가된 메서드가 됨
        print('B.__methodB')

def main():
    ob = B()
    print(dir(ob))
    A._A__methodB(ob) #직접 호출은 가능하나 의미없음
    B._B__methodB(ob) #직접 호출은 가능하나 의미없음
    
main()


