
# < 세트 >
# set(집합)는 순서가 없고, 중복을 허용하지 않는 가변(mutable) 데이터 구조
# 중복을 제거하는 데 사용할 수 있음
# set(집합)는 중괄호 { }를 사용하여 표현
# 요소들은 쉼표, 로 구분

# 빈 set 생성
empty_set = set()

# 정수형 set 생성
numbers = {1, 2, 3, 4, 5}

# 문자열 set 생성
fruits = {"apple", "banana", "cherry"}

# 다양한 자료형이 포함된 set 생성
mixed_set = {1, "apple", 3.14}

# set에 요소 추가 (add)
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)       # {'apple', 'banana', 'cherry', 'orange'}

# set에서 요소 제거 (remove)
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)       # {'apple', 'cherry'}


# 집합 연산
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 합집합
print(A | B)  # {1, 2, 3, 4, 5, 6, 7, 8}

# 교집합
print(A & B)  # {4, 5}

# 차집합
print(A - B)  # {1, 2, 3}

# 대칭차집합 (교집합의 반대개념)
print(A ^ B)  # {1, 2, 3, 6, 7, 8}
