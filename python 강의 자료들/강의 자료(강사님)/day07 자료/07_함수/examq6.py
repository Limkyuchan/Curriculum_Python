#수를 입력 받아 1부터 입력한 수 사이의 2의 배수들의 합을 반환하는 함수
def nSum(n):
    sumVal = 0
    for i in range(1, n):
        if i%2 == 0:
            sumVal += i
    return sumVal

print( nSum(10) )
print( nSum(5) )
