class A:
    def methodA(self):
        print('methodA')
    def methodB(self):
        print('methodB')
        self.methodA()

class B(A):
    def methodBA(self):
        print('B.methodBA')
        self.methodB()
    def methodA(self):
        print('B.methodA')
        self.methodB()
    def methodB(self):
        print('B.methodB')

def main():
    ob = B()
    print(dir(ob))
    ob.methodBA()
    ob.methodA()
    ob.methodB()

main()




