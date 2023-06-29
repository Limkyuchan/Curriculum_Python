
# < Comprehension >
# Comprehension은 리스트, 사전, 집합 등에서 활용
# - 파이썬에서 매우 자주 사용되는 문법 중 하나
# - 반복 가능한 객체(iterable object)의 각 항목에 대해 표현식을 평가하여
#   새로운 리스트, 사전, 집합을 간단하고 읽기 쉽게 생성하는 방법
# - 특정 유형의 반복문을 단순화하고 최적화하여 코드를 간단하게 만들고 가독성을 높임
# - 다양한 컬렉션 타입을 간단하게 생성할 수 있도록 도와줌
# - 파이썬을 사용할 때는 컴프리헨션을 적극적으로 활용하는 것이 좋음
# - 표현 방식
#       리스트(list) : 대괄호 [ ]
#       사전(dict) : 중괄호 { }
#       집합(set) : 소괄호 ( )
# 리스트 Comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers) # Output: [1, 4, 9, 16, 25] 

# 사전 Comprehension
word = "Hello"
word_dict = {char: word.count(char) for char in word} 
print(word_dict) # Output: {'H': 1, 'e': 1, 'l': 2, 'o': 1} 

# 집합 Comprehension
numbers = [1, 2, 3, 2, 1]
unique_numbers = {n for n in numbers}
print(unique_numbers) # Output: {1, 2, 3}



# 1) List Comprehension(리스트 컴프리헨션)
#   형식: [표현식 for 항목 in iterable if 조건문]
#     표현식: 각 항목에서 계산되어 리스트의 요소가 될 값
#     항목: iterable 객체의 각 요소를 차례대로 지정하는 변수
#     조건문: 항목이 조건문을 만족할 때만 표현식이 계산되어 리스트의 요소가 됨(생략 가능) 
# 예시)
# 1부터 5까지의 숫자를 담은 리스트를 생성하는 방법
numbers = [num for num in range(1,6)]
print(numbers)  # 출력: [1, 2, 3, 4, 5]

# 리스트를 생성하면서 조건문을 함께 사용하는 방법
evens = [num for num in range(1, 11) if num % 2 == 0]
print(evens)  # 출력: [2, 4, 6, 8, 10]

"""
if - else 조건문이 for문 앞에 위치한다. 
형식: [ 출력값1 if 조건식 else 출력값2 for 항목 in iterable ]
"""

# 2) Dictionary Comprehension(딕셔너리 컴프리헨션)
#   형식: {키: 값 for 항목 in iterable if 조건문}
#     항목: iterable 객체의 각 요소를 차례대로 지정하는 변수
#     조건문: 항목이 조건문을 만족할 때만 표현식이 계산되어 딕셔너리의 요소가 됨(생략 가능) 
#     키: 딕셔너리의 키(key)가 되는 값
#     값: 딕셔너리의 값(value)이 되는 값
# 예시)
# 1부터 5까지의 숫자를 키로 하고, 각 숫자의 제곱을 값으로 갖는 딕셔너리를 생성하는 방법
squares = {num: num ** 2 for num in range(1, 6)}
print(squares)  # 출력: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 딕셔너리를 생성하면서 조건문을 함께 사용하는 방법
even_squares = {num: num ** 2 for num in range(1, 11) if num % 2 == 0}
print(even_squares)  # 출력: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# 3) Set Comprehension(집합 컴프리헨션)
#   형식: {표현식 for 항목 in iterable if 조건문}
#     표현식: 각 항목에서 계산되어 집합의 요소가 될 값
#     항목: iterable 객체의 각 요소를 차례대로 지정하는 변수
#     조건문: 항목이 조건문을 만족할 때만 표현식이 계산되어 집합의 요소가 됨(생략 가능)
# 리스트와 동일하지만 중복 값이 제거된 집합을 생성
# 예시)
# 1부터 5까지의 숫자를 담은 집합을 생성하는 방법
list = [1, 2, 3, 4, 5, 6, 1, 2, 2, 3, 4]
numbers = {num for num in list}
print(numbers)  # 출력: {1, 2, 3, 4, 5, 6}

# 집합을 생성하면서 조건문을 함께 사용하는 방법
odds = {num for num in range(1, 11) if num % 2 == 1}
print(odds)  # 출력: {1, 3, 5, 7, 9}
