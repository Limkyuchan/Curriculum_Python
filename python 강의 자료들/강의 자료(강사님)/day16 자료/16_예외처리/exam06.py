# multi except 적용 방법 - 1
try:
    n1 = int(input('수 입력:'))
    n2 = int(input('수 입력:'))
    ret = n1 / n2
except ZeroDivisionError as msg:
    print('예외:', msg)
except ValueError as msg:
    print('예외:', msg)

print(f'{n1}/{n2}={ret}')

# multi except 적용 방법 - 2
try:
    n1 = int(input('수 입력:'))
    n2 = int(input('수 입력:'))
    ret = n1 / n2
except (ZeroDivisionError, ValueError) as msg:
    print('예외:', msg)

print(f'{n1}/{n2}={ret}')

