
# maintest.py

print("maintest.__name__ :", __name__)
# maintest 에서 실행했을 때의 __name__


import mymodule     

result = mymodule.mysum(10, 20)
print(result)

result = mymodule.mymin(10, 20)
print(result)