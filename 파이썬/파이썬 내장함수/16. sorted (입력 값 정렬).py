
# < sorted >
# 입력 값 정렬 후 결과를 리스트로 반환하는 함수
# 리스트 자료가 가지는 sort()함수는 반환이 없음

print('오름차순')
n = sorted([3,1,2])
print(n)

n = sorted(['a', 'c', 'b'])
print(n)

n = sorted('zero')
print(n)

n = sorted((3,2,1))
print(n)


n = [3,1,2]
ret = n.sort()      
print(ret)          # sort는 반환값이 없고, 그 자체가 변환된다.
print(n)            # n 값이 변경됨


print('내림차순')
n = sorted(['a', 'c', 'b'], reverse = True)
print(n)

n = [3,1,2]
ret = n.sort(reverse = True)
print(ret)          # sort는 반환값이 없고, 그 자체가 변환된다.
print(n)            # n 값이 변경됨
