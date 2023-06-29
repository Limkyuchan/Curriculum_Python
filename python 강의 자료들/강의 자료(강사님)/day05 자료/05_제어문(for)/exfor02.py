num1 = int(input('값 입력:'))
for i in range(0, num1 + 1):
    if i%2 == 1:
        print(i)

print()

num1 = int(input('값 입력:'))
for i in range(0, num1 + 1):
    if i%2 == 1:
        print(i, ':홀수')
    else:
        print(i, ':짝수')

print()

num1 = int(input('30이하의 수 입력:'))
if num1 <= 30:
    sumval = 0
    for i in range(num1, 31):
        if i%3 == 0:
            sumval += i
    print('sumval = {0}'.format(sumval))
else:
    print('30이하의 수를 입력하세요.')

print()

num1 = int(input('높이 입력(라인 수):'))
star = ''
for i in range(0, num1):
    star += '★'
    print(star)