class A:
    def __init__(self):
        print('A생성자')
    def methodA(self):
        print('methodA()')

class B(A):
    def __init__(self):
        print('B생성자')
    def methodA(self):
        print('methodA() - B')
    def methodB(self):
        print('methodB()')

class C(A):
    def __init__(self):
        print('C생성자')
    def methodC(self):
        print('methodC()')

class D(B, C): #다중 상속
    def __init__(self):
        print('AB생성자')
    def methodAB(self):
        print('methodAB()')

ob = D()
ob.methodA()
ob.methodB()
ob.methodC()
ob.methodAB()