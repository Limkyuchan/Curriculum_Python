#인자로 N을 전달하면 N에 대한 팩토리얼을 반환하는 함수 정의
# 팩토리얼은 1부터 n까지 곱한 수
# ex) 4 팩토리얼(4!라고 표현)은 = 1*2*3*4 = 24

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact

print( factorial(3) )
print( factorial(4) )
print( factorial(5) )
print( factorial(6) )