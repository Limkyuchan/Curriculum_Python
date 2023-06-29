
# < map >
# map(f, iterable)
# 함수(f)와 반복 가능한(iterable) 자료형을 받음
# 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 반환

def two_times(x):
    return x*2

n = list(map(two_times, [1,2,3,4]))
print(n)

n = list(map(lambda a:a+1, n))
print(n)



# 여러 숫자 입력받기

a, b, c = map(int, input("수 입력: ").split())
print(a, b, c)