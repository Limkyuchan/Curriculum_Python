
# < lambda >
# 함수를 생성할 때 사용하는 예약어
# - def와 동일한 역할
# - 일반적으로 함수를 한 줄로 간결하게 만들 때 사용
# - def를 사용해야 할 만큼 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰임

mysum = lambda a,b:a+b
print(mysum(1, 2))

mylist = [lambda a,b:a+b, lambda a,b:a*b]
print(mylist[0](3,4))
print(mylist[1](3,4))