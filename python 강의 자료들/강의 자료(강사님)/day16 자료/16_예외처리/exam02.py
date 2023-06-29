
n1 = int(input('수 입력:'))
n2 = int(input('수 입력:'))

try:
    ret = n1 / n2
except ZeroDivisionError:
    print('정수를 0으로 나눌 수 없음')

print(f'{n1}/{n2}={ret}')

