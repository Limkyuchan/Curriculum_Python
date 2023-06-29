data = input('정수를 입력하세요')

# 슬라이싱 활용
result1 = data[::-1]
print(f'{data}의 거꾸로 수는 {result1}입니다.')

# 반복문 활용1
result2 = ''
for i in range(len(data)-1, -1, -1):
    result2 += data[i]
print(f'{data}의 거꾸로 수는 {result2}입니다.')

#반복문 활용2
result3 = ''
i = len(data)-1
while i > -1:
    result3 += data[i]
    i -= 1
print(f'{data}의 거꾸로 수는 {result3}입니다.')

# 연산자를 활용하는 방법
result4 = 0
tmp = int(data)
while True:
    result4 += tmp % 10
    tmp = tmp // 10
    if tmp == 0:
        break
    result4 *= 10

print(f'{data}의 거꾸로 수는 {result4}입니다.')