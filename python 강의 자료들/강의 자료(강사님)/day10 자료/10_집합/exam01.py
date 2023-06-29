"""
집합(Set)은 순서가 없고 
중복을 허용하지 않는 가변(mutable) 데이터 구조
중복을 제거하는 데 사용할 수 있음
집합은 중괄호({})를 사용하여 표현
요소들은 쉼표(,)로 구분
"""
# 집합 생성 및 초기화
empty_set = set()  # 빈 집합 생성
numbers = {1, 2, 3, 4, 5}  # 정수형 집합 생성
fruits = {"apple", "banana", "cherry"}  # 문자열 집합 생성
mixed_set = {1, "apple", 3.14}  # 다양한 자료형이 포함된 집합 생성

print(empty_set)
print(numbers)
print(fruits)
print(mixed_set)