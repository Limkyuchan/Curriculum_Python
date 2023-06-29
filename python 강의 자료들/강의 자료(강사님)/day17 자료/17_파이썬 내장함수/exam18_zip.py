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
