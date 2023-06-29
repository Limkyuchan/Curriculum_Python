import random

numbers = list(range(1, 46))  # 1부터 45까지의 숫자를 포함하는 리스트 생성
lotto_num = random.sample(numbers, 6)  # 리스트에서 중복 없이 6개의 숫자를 무작위로 선택
lotto_num.sort()  # 선택된 숫자를 오름차순으로 정렬

print(lotto_num)
