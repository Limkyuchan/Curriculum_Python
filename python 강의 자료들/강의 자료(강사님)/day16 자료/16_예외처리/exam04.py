
n1 = int(input('수 입력:'))
n2 = int(input('수 입력:'))

try:
    ret = n1 / n2
    print('예외가 발생되면 출력되지 않음')
except ZeroDivisionError:
    print('정수를 0으로 나눌 수 없음')
else:
    print('예외 없음')

print(f'{n1}/{n2}={ret}')

