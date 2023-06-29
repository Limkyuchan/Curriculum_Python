
# 함수

# Q1. 임의의 개수로 실수를 입력 받아 최소값과 최대값을 제외한 나머지 점수들의 합계를 
#     반환하는 함수를 정의 (단, 가변인자를 활용)

def add(*su):
    hap = 0

    for i in su:
        hap += i
    return hap - (max(su) + min(su))

n = int(input("입력할 수의 개수? "))

li = []
for i in range(n):
    li.append(float(input("실수 입력: ")))
    
print(f"최대값, 최소값을 제외한 수들의 합은 {add(*li)}")


# Q2. 합계에 해당하는 값과 개수를 입력 받아 평균을 반환하는 함수 정의

def avg(x, y):
    return round(x / y , 2)

total = float(input("합계? "))
su = int(input("입력한 수의 개수: "))

print(f"평균은 {avg(total, su)}")


# Q3. cm값을 inch 값으로 반환하는 함수 정의 (1 inch == 2.54cm)

def inch(x):
    return round(x / 2.54, 5)

su = int(input("cm 입력: "))
print(f"{su}cm는 {inch(su)}inch")


# Q4. 파일의 용량(byte)을 매개변수로 입력 받아 bit단위로 반환하는 함수 정의
#     파일의 용량을 입력할 때 단위도 입력한다.(G, M, K)
#     ex) byteToBit(32, "G")   byteToBit(64, "M")

def bit(x, y):
    if y == "G" or y == "g":
        return x * (1024**3) * 8
    elif y == "M" or y == "m":
        return x * (1024**2) * 8
    elif y == "K" or y == "k":
        return x * 1024 * 8

file = int(input("파일 용량 입력: "))
file2 = input("파일 단위(G, M, K) 입력: ")
print(f"{file}{file2}B는 {bit(file, file2)}bit")


# Q5. 인자로 N을 전달하면 N에 대한 팩토리얼을 반환해주는 함수 정의

def 팩토(N):
    su = 1
    for i in range(1,N+1):
        su *= i
    return su

N = int(input("수 입력: "))
print(f"{N}의 팩토리얼 값은 {팩토(N)}")


# Q6. 인자로 N을 전달하면 거꾸로 만든 수를 반환하는 함수 정의

def 거꾸로(N):
    result = 0
    while True:
        result += N % 10
        N = N // 10

        if N == 0:
            break
        result *= 10
    return result

N = int(input("수 입력: "))
print(f"{N}을 거꾸로 하면 {거꾸로(N)}")



# N = input("입력: ")

# def 거꾸로(N):
#     N = N[::-1]
#     return N

# print(거꾸로(N))