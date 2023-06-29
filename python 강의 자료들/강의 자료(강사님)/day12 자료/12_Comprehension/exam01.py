"""
Comprehension은 리스트, 사전, 집합 등의 
- 파이썬에서 매우 자주 사용되는 문법 중 하나
- 반복 가능한 객체(iterable object)의 각 항목에 대해 
  표현식을 평가하여 새로운 리스트, 사전, 집합을 간단하고 읽기 쉽게 생성하는 방법
- 특정 유형의 반복문을 단순화하고 최적화하여 코드를 간단하게 만들고 가독성을 높임
- 다양한 컬렉션 타입을 간단하게 생성할 수 있도록 도와줌
- 파이썬을 사용할 때는 컴프리헨션을 적극적으로 활용하는 것이 좋음

표현 방식
    리스트: 대괄호 [ ]
    사전: 중괄호 { }
    집합: 괄호 ( )
"""
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
