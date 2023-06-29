
# maintest.py

# 표현방식 4)
# as 를 사용하여 별칭을 정해 사용하기
from mymodule import mysum as ms
import mymodule as mm

result = ms(10, 20)
print(result)

result = mm.mymin(10, 20)
print(result)