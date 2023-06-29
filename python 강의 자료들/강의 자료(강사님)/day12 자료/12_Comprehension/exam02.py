# List Comprehension(리스트 컴프리헨션)
# 형식 - [표현식 for 항목 in iterable if 조건문]
#   표현식: 각 항목에서 계산되어 리스트의 요소가 될 값
#   항목: iterable 객체의 각 요소를 차례대로 지정하는 변수
#   조건문: 항목이 조건문을 만족할 때만 표현식이 계산되어 리스트의 요소가 됨(생략 가능)

# 1부터 5까지의 숫자를 담은 리스트를 생성하는 방법
numbers = [num for num in range(1, 6)]
print(numbers)  # 출력: [1, 2, 3, 4, 5]

# 리스트를 생성하면서 조건문을 함께 사용하는 방법
evens = [num for num in range(1, 11) if num % 2 == 0]
print(evens)  # 출력: [2, 4, 6, 8, 10]
