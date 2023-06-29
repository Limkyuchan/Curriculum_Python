# Dictionary Comprehension(딕셔너리 컴프리헨션)
# 형식 - {키: 값 for 항목 in iterable if 조건문}
#   표현식: 각 항목에서 계산되어 딕셔너리의 요소가 될 값
#   항목: iterable 객체의 각 요소를 차례대로 지정하는 변수
#   조건문: 항목이 조건문을 만족할 때만 표현식이 계산되어 딕셔너리의 요소가 됨(생략 가능)
#   키: 딕셔너리의 키(key)가 되는 값
#   값: 딕셔너리의 값(value)이 되는 값
 
# 1부터 5까지의 숫자를 키로 하고, 각 숫자의 제곱을 값으로 갖는 딕셔너리를 생성하는 방법
squares = {num: num ** 2 for num in range(1, 6)}
print(squares)  # 출력: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 딕셔너리를 생성하면서 조건문을 함께 사용하는 방법
even_squares = {num: num ** 2 for num in range(1, 11) if num % 2 == 0}
print(even_squares)  # 출력: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
