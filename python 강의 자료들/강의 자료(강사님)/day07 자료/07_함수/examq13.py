#인자로 N을 전달하면 거꾸로 만든 수를 반환하는 함수 정의

def reverseNum(n):
    ret = 0
    while n != 0:
        tmp = n%10
        ret *= 10
        ret += tmp
        n //= 10
    return ret

print( reverseNum(123) )
print( reverseNum(123)+1 )
print( reverseNum(321) )
print( reverseNum(321)+1 )
