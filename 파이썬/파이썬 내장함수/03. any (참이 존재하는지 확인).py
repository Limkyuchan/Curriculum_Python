
# < any - or 연산>
# 반복 가능한 자료를 받아 자료 중 참이 존재하는지를 확인하는 함수

n = any([1,2,3,0])
print(n)

n = any([0, "", 0.0, None, False])
print(n)