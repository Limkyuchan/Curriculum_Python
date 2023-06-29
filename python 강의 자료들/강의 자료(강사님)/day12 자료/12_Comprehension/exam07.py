# 컴프리핸션에 람다 함수 활용

# 람다 함수 정의
power = 3
power_function = lambda x: x ** power

# 리스트 컴프리헨션을 사용하여 세제곱수 생성
cubes = [power_function(num) for num in range(1, 11)]
print("Cubes:", cubes)

# 리스트 컴프리헨션을 사용하여 람다 함수 리스트 생성
list = [lambda x: x*2 for x in range(1, 5)]
print(list[0](2))
print(list[1](4))
print(list[2](6))
print(list[3](8))
