import random as rd

# 개선된 코드
lotto_num = []
i = 0
while i < 6:
    num = rd.randint(1, 45)  # 무작위로 숫자를 생성
    is_duplicate = False
    for j in range(i):
        if num == lotto_num[j]:  # 중복 확인
            is_duplicate = True
            break
    if not is_duplicate:  # 중복이 없으면 리스트에 추가
        lotto_num.append(num)
        i += 1

lotto_num.sort()
print(lotto_num)
