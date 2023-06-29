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

class C(B):
    def __init__(self):
        print('C생성자')
    def methodC(self):
        print('methodC()')

class D(C):
    def __init__(self):
        print('D생성자')
    def methodD(self):
        print('methodD()')

A().methodA()
print()
obB = B()
obB.methodB()
obB.methodA()
print(dir(obB))
print()
obD = D()
obD.methodA()