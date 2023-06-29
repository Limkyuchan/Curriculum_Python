import random as rd

# 정직한 코드
lotto_num = []
i = 0
while i < 6:
    lotto_num.append(rd.randint(1, 45))
    j = 0
    while i < j:
        if lotto_num[i] == lotto_num[j]:
            lotto_num.pop(i)
            i -= 1
            break
        j += 1
    i += 1

lotto_num.sort()
print(lotto_num)

