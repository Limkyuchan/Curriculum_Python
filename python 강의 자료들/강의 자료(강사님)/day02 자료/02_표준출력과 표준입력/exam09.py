#서식 출력 format함수
name = '홍길동'
age = 20
pi = 3.14
n = 10

fmt = "{0},{1},{2}"
print('이름: {0}'.format(name))
print('나이: {0}세'.format(age))
print('PI: {0}'.format(round(pi,1)))
print('PI: {0:10.4f}'.format(pi))
print(fmt.format(n,n,n))

print('이름: [{0:<10}]'.format(name))
print('이름: [{0:>10}]'.format(name))
print('이름: [{0:^10}]'.format(name))
print('이름: [{0:!^10}]'.format(name))



