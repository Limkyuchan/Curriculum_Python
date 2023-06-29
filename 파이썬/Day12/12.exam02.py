
# < 튜플 컴플리헨션 제너레이터 표현식>
# - 파이썬에서는 튜플 컴프리헨션(tuple comprehension)을 지원하지 않음
# - 튜플은 불변(immutable)하기 때문에 컴프리헨션을 통해 값을 생성할 수 없음
# - 하지만 제너레이터 표현식(generator expression)을 사용하면 튜플 생성 가능
# - 제너레이터 표현식은 컴프리헨션과 비슷하지만, 괄호()를 사용하여 생성하며,
#   값을 미리 생성하지 않고 필요할 때마다 생성

# 제너레이터 컴프리헨션
#  형식: (표현식 for 항목 in iterable if 조건문)
#    표현식: 각 항목에서 계산되어 튜플의 요소가 될 값
#    항목: iterable 객체의 각 요소를 차례대로 지정하는 변수
#    조건문: 항목이 조건문을 만족할 때만 표현식이 계산되어 튜플의 요소가 됨(생략 가능)
# 결과 값이 제네레이터를 생성


# 예시 1) 제너레이터 표현식으로 튜플 생성하기
t = tuple(x for x in range(1, 6))
print(t)  # 출력: (1, 2, 3, 4, 5)

# range() 함수로 1부터 5까지의 숫자를 생성하고, 
# 이를 제너레이터 표현식을 사용하여 튜플로 생성
# 이때 tuple() 함수를 사용하여 제너레이터 표현식을 튜플로 변환

# 예시 2) 제너레이터 컴프리헨션
squares_gen = (num ** 2 for num in range(1, 6))
print(squares_gen)  # 출력: <generator object <genexpr> at 0x7f37f8b32e40>
print(list(squares_gen))  # 출력: [1, 4, 9, 16, 25]

# squares_gen 변수에는 
# <generator object <genexpr> at 0x7f37f8b32e40>과 같은 제너레이터 객체가 생성됨
# list(), tuple(), set() 등의 함수를 사용하여 제너레이터에서 값을 하나씩 꺼내 사용할 자료로 변환. 

