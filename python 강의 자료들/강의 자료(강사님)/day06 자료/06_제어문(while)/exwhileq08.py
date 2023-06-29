decimal = int(input("십진수 입력: "))

bin = ""

while decimal > 0:
    remainder = decimal % 2
    bin = str(remainder) + bin 
    decimal //= 2

# 결과 출력
print(bin)