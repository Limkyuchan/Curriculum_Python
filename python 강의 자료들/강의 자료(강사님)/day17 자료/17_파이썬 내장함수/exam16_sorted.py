print('오름차순')
n = sorted([3,1,2])
print(n)
n = sorted(['a', 'c', 'b'])
print(n)
n = sorted('zero')
print(n)
n = sorted((3,2,1))
print(n)

n = [3,1,2]
ret = n.sort()
print(ret)
print(n)

print('내림차순')
n = sorted(['a', 'c', 'b'], reverse=True)
print(n)

n = [3,1,2]
ret = n.sort(reverse=True)
print(ret)
print(n)
