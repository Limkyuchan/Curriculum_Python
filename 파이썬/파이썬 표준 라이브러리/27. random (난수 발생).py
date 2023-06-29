
# < random >
# 난수를 발생시키는 모듈
# random() - 0.0 ~ 1.0 사이의 난수
# randint(x, y) - x ~ y 사이의 난수
# shuffle(data) - 리스트의 값을 무작위로 섞기

import random

n = random.random()
print('0.0 ~ 1.0 사이의 난수:', n)

n = random.randint(1, 10)
print('1 ~ 10 사이의 난수:', n)

lst = [5,1,3,2,4]
random.shuffle(lst)
print('섞기:', lst)
