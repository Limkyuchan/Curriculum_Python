# 람다 함수 활용 예시
def universal_calc(a, b, func=None):
    if not func:
        return -1
    return func(a, b)

add = lambda a, b: a + b

ret1 = universal_calc(1, 2, func=add)
ret2 = universal_calc(2, 2, func=lambda x, y: x * y)

print(ret1)
print(ret2)