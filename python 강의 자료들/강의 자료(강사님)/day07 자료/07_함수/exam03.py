def oddEven(val):
    ret = ""
    if val%2 == 0:
        ret = "짝수"
    else:
        ret = "홀수"
    return ret

def scope(start, end, val):
    if val >= start and val <= end:
        return True
    else:
        return False

print(oddEven(3))
print(oddEven(4))

print(scope(1, 100, 89))
print(scope(1, 100, 110))
