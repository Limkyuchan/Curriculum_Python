s = input('문자 입력:')
for i in range(1, 6):
    print(f'{i}.{s}')
print()

n = int(input('수 입력:'))
ret = 0
for i in range(1, n+1):
    ret += i

print(f'1~{n}까지의 합:{ret}')
print()

n = int(input('수 입력:'))
for i in range(n, -1, -1):
    print(i)
