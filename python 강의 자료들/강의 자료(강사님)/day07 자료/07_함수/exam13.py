# mutable(변경 가능한)
def func(a):
    a[0] = 'HELLO'

a = ['hello', 'hi']
print(a)
func(a)
print(a)
print()

# immutable(변경 불가능한) - 기본 자료형
def func(a):
    print('func2:', id(a))
    a = 'HELLO'
    print('func3:', id(a))
    print('func:', a)

a = 'hello'
print('global1:', id(a))
print(a)
func(a)
print(a)
print('global:4', id(a))


# immutable(변경 불가능한) - 투플 자료형
def func(a):
    #a[0] = 'HELLO' #요소 변경 불가(튜플 요소 변경 시 Error!)
    a = (1,2,3) #참조 대상을 변경하는 것은 가능
    print('func:', a)

a = ('hello', 'hi')
print(a)
func(a)
print(a)
