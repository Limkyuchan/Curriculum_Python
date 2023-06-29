#숫자를 입력 받아 절대값을 반환하는 함수 정의

def myAbs(n):
    if n < 0:
        n *= -1
    return n

print(abs(-3))
print( myAbs(4) )
print( myAbs(-4) )
