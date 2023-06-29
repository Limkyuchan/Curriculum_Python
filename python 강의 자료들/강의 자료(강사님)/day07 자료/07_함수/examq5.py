#1부터 입력한 수까지의 합을 반환하는 함수 정의
def nSum(n):
    sumVal = 0
    for i in range(1, n+1):
        sumVal += i
    return sumVal

print( nSum(10) )
print( nSum(5) )
