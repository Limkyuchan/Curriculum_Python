# 10이하의 정수를 5개 입력 받아 짝수이면 출력
for i in range(0, 5):
    n = int(input('정수 입력:'))
    if n%2 == 0:
        print(n)
print()

# 수를 입력 받아 1부터 입력한 수 사이의 2의 배수를 출력
n = int(input('수 입력:'))
for i in range(2, n):
    if i%2 == 0:
        print(i)
print()

# 수를 입력 받아 1부터 입력한 수 사이의 3의 배수를 출력
n = int(input('수 입력:'))
for i in range(2, n):
    if i%3 == 0:
        print(i)
print()

# 수를 입력 받아 1부터 입력한 수 사이의 2의 배수와 3의 배수를 출력
n = int(input('수 입력:'))
for i in range(2, n):
    if i%2 == 0 or i%3 == 0:
        print(i)
print()

# 수를 입력 받아 1부터 입력한 수 사이의 2와 4의 공배수를 출력
n = int(input('수 입력:'))
for i in range(2, n):
    if i%4 == 0 and i%2 == 0:
        print(i)
print()

# 5개의 점수를 입력 받아 최대값을 출력
maxval = 0
for i in range(0, 5):
    n = int(input('수 입력:'))
    if maxval < n:
        maxval = n
print(f'입력한 수 중 최대값:{maxval}')
print()

# 100이하의 점수 5개를 입력 받아 최소값을 구하시오
minval = 100
for i in range(0, 5):
    n = int(input('수 입력(100이하):'))
    if n < minval:
        minval = n
print(f'입력한 점수 중 최소값:{minval}')
print()

# 5개의 점수를 입력 받아 최대값과 최소값을 제외한 나머지 점수의 합계와 평균을 구하시오
maxval = 0
minval = 0
sumval = 0
for i in range(0, 5):
    n = int(input('점수 입력:'))
    if i == 0:
        maxval = n
        minval = n
    if n < minval:
        minval = n
    if n > maxval:
        maxval = n
    sumval += n

sumval -= (maxval + minval)
avgval = sumval / 3
print(f'합계: {sumval}')
print(f'평균: {avgval:0.3f}')


# 100이하의 점수 5개를 입력 받아 최소값을 구하시오(다시 입력 적용)
minval = 100
i = 0
while i != 5:
    n = int(input('수 입력(100이하):'))
    if n > 100:
        print('입력 범위를 확인하세요.')
        i -= 1
    if n < minval:
        minval = n
    i += 1
    print(i)    
print(f'입력한 점수 중 최소값:{minval}')
print()

