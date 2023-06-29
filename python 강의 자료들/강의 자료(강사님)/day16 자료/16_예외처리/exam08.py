try:
    n1 = int(input('수 입력:'))
    n2 = int(input('수 입력:'))
    if n2 == 0:
        raise ValueError('입력문제')
    ret = n1 / n2
except ValueError as msg:
    print('예외:', msg)

print(f'{n1}/{n2}={ret}')

