#팩토리얼 구하는 함수를 재귀로 구현

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


print( factorial(0) )
print( factorial(1) )
print( factorial(3) )
print( factorial(4) )
print( factorial(5) )




