
# < filter >
# 첫 번째 인수: 함수 이름
# 두 번째 인수: 그 함수에 차례로 들어갈 반복 가능한 자료형
#   ex) filter(함수 이름, 반복 가능 자료형)
# 두 번째 인수의 요소들이 첫 번째 인수인 함수에 입력되었을 때 리턴값이 참인 것만 묶어서(걸러내서) 반환

# 예시 1) 직접 구현
def positive1(lst):
    result = []
    for i in lst:
        if i > 0:
            result.append(i)
    return result

print(positive1([1,-3,2,0,-5,6]))
print()

# 예시 2)
def positive2(lst):
    return lst > 0

d = [1,-3,2,0,-5,6]
n = list(filter(positive2, d))
print(n)
print()

# 예시 3)
positive3 = lambda x: x > 0
n = list(filter(positive3, [1,-3,2,0,-5,6]))
print(n)
print()

# 예시 4)
n = list(filter(lambda x: x > 0, [1,-3,2,0,-5,6]))
print(n)