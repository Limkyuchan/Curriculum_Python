#거꾸로 수를 반환하는 함수(재귀)

def digit_count(n):
    cnt = 1
    if n == 0:
        return 0
    else:
        cnt += digit_count(n//10)
        return cnt

def reverse_num(n):
    rn = n%10
    if n == 0:
        return n
    else:
        rn *= 10 ** (digit_count(n)-1)
        rn += reverse_num(n//10)
        return rn

print(reverse_num(1))
print(reverse_num(123))
print(reverse_num(1234))
print(reverse_num(44336655771122))