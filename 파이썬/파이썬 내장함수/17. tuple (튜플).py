
# < tuple >
# 반복 가능한 자료형을 입력받아 tuple 형태로 반환하는 함수
# tuple을 받으면 그대로 tuple을 반환

n = tuple("abc")
print(n)

n = tuple([1,2,3])
print(n)

n = tuple((1,2,3))
print(n)

# n = tuple((1)) # 에러! 튜플은 하나의 원소를 가지는 경우 마지막에 ,(콤마) 필요
n = tuple((1,))
print(n)