try:
    n1 = int(input('수 입력:'))
    n2 = int(input('수 입력:'))
    ret = n1 / n2
except (ZeroDivisionError, ValueError) as msg:
    pass

print(f'{n1}/{n2}={ret}')

