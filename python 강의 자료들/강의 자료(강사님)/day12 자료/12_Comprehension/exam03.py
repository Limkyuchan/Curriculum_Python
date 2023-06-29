# Set Comprehension(집합 컴프리헨션)
# 형식 - {표현식 for 항목 in iterable if 조건문}
#   표현식: 각 항목에서 계산되어 집합의 요소가 될 값
#   항목: iterable 객체의 각 요소를 차례대로 지정하는 변수
#   조건문: 항목이 조건문을 만족할 때만 표현식이 계산되어 집합의 요소가 됨(생략 가능)
# 리스트와 동일하지만 중복 값이 제거된 집합을 생성   

# 1부터 5까지의 숫자를 담은 집합을 생성하는 방법
list = [1, 2, 3, 4, 5, 6, 1, 2, 2, 3, 4]
numbers = {num for num in list}
print(numbers)  # 출력: {1, 2, 3, 4, 5, 6}

# 집합을 생성하면서 조건문을 함께 사용하는 방법
odds = {num for num in range(1, 11) if num % 2 == 1}
print(odds)  # 출력: {1, 3, 5, 7, 9}
