
"""
컴프리헨션은 파이썬의 특징 중 하나!
코드를 간결하게 작성할 수 있으며 가독성을 높일 수 있음.
중첩된 컴프리헨션은 오히려 가독성이 떨어지기 때문에 중첩이 필요한 경우 별도의 변수를 사용하는 것을 권장.
컴프리헨션에서는 일반적으로 한 줄에 들어갈 정도로 간단한 표현식을 사용!!
"""

# < 중첩된 리스트 컴프리헨션 >
# 중첩된 리스트 컴프리헨션을 사용하여 2차원 리스트를 생성하는 코드
matrix = [[row * 3 + col for col in range(3)] for row in range(3)]
print(matrix)  # 출력: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]





# < 컴프리핸션에 람다 함수 활용 >
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


