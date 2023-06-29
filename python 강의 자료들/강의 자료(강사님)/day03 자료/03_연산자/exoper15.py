num = int(input('1 ~ 100범위의 수 입력:'))
ret = num <= 100 and num >= 1 and '참' or '거짓'
print('num =', num, ret)

num1 = int(input('첫 번째 수:'))
num2 = int(input('첫 번째 수:'))
ret = num1 >= num2 and num1 or num2
print(f'{num1}, {num2}중 큰 수는 {ret}이다.')