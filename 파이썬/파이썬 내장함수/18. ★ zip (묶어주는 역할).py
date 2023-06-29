
# < zip >
# 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
# 같은 위치의 값은 튜플로 묶임

n = list(zip([1,2,3], [4,5,6]))
print(n)

t1 = ('a','b','c')
t2 = ('z','x','y')
n = tuple(zip(t1, t2))
print(n)

t2 = ('z', 'x')
n = tuple(zip(t1, t2))
print(n)

l1 = ['z','x','y']
n = list(zip(t1, l1))
print(n)

l2 = ['z','x','y']
n = list(zip(l2, t1))
print(n)
