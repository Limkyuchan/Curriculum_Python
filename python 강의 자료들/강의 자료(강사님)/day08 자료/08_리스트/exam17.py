"""
파이썬의 리스트(List)는 가변적이고 순차적인 데이터 구조
여러 값들을 저장하고 관리
리스트를 만들 때는 []를 사용
리스트의 각 요소는 ,로 구분
"""

# 리스트 생성하기 및 초기화
empty_list = []  # 빈 리스트 생성, list()
numbers = [1, 2, 3, 4, 5]  # 정수형 리스트 생성
fruits = ["apple", "banana", "cherry"]  # 문자열 리스트 생성
mixed_list = [1, "apple", 3.14]  # 다양한 자료형이 포함된 리스트 생성

print(empty_list)
print(numbers)
print(fruits)
print(mixed_list)

# 리스트 인덱싱(Indexing)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # "apple"
print(fruits[1])  # "banana"
print(fruits[-1])  # "cherry" (음수 인덱스는 뒤에서부터 인덱싱)

# 리스트 슬라이싱(Slicing)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1:4])  # [1, 2, 3] (인덱스 1부터 3까지 슬라이싱)
print(numbers[:3])  # [0, 1, 2] (처음부터 인덱스 2까지 슬라이싱)
print(numbers[4:])  # [4, 5, 6, 7, 8, 9] (인덱스 4부터 끝까지 슬라이싱)
print(numbers[::2])  # [0, 2, 4, 6, 8] (처음부터 끝까지 2씩 건너뛰며 슬라이싱)

# 리스트 길이 확인
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # 3

# 리스트에 요소 추가 및 삭제
fruits = ["apple", "banana", "cherry"]

# 요소 추가
fruits.append("orange")  # ["apple", "banana", "cherry", "orange"]
print(fruits)

# 요소 삭제
fruits.remove("banana")  # ["apple", "cherry", "orange"]
print(fruits)
del fruits[1]  # ["apple", "orange"]
print(fruits)

# 리스트 정렬
numbers = [5, 3, 1, 4, 2]
numbers.sort()  # [1, 2, 3, 4, 5]
print(numbers)
numbers.sort(reverse=True)  # [1, 2, 3, 4, 5]
print(numbers)

fruits = ["banana", "apple", "cherry"]
fruits.sort()  # ["apple", "banana", "cherry"]
print(fruits)

# 리스트에 요소 삽입
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")  # 인덱스 1에 "orange" 삽입
print(fruits)  # ["apple", "orange", "banana", "cherry"]

# 리스트에서 요소 꺼내기
fruits = ["apple", "banana", "cherry"]
removed_item = fruits.pop(1)  # 인덱스 1의 요소를 제거하고 반환
print(removed_item)  # "banana"
print(fruits)  # ["apple", "cherry"]

# 리스트에서 특정 값의 인덱스 찾기
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")
print(index)  # 1

# 리스트에서 특정 값의 개수 세기
numbers = [1, 2, 3, 2, 1, 3, 1, 1, 2, 3]
count = numbers.count(1)
print(count)  # 4 (1이 4번 등장)

# 리스트 반전
numbers = [3, 4, 5, 1, 2]
numbers.reverse()
print(numbers)  # [2, 1, 5, 4, 3]


# 리스트 확장
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(id(list1))
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]
print(id(list1))

list3 = [1, 2, 3]
list4 = [4, 5, 6]
print(id(list3))
#list3 = list3 + list4
list3 += list4
print(list3)  # [1, 2, 3, 4, 5, 6]
print(id(list3))

# 리스트 복사(mutable)
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)  # [1, 2, 3]
print(id(original_list))
print(id(copied_list))

# 리스트의 모든 요소 삭제
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # []


# 리스트 반복문
numbers = [1,5,2,3,4]
for n in range(len(numbers)):
    print(numbers[n])
print()

numbers = [1,5,2,3,4]
for n in numbers:
    print(n)
print()

# 다차원 리스트
lst = [
    [1, 2, 3],
    [4, 5, 6],
]

print(lst)
print(lst[0])
print(lst[1])

print(lst[1][2])

lst2 = [1, 2, 3, [4, 5, 6]]

print(lst2)
print(lst2[0])
print(lst2[1])
print(lst2[2])
print(lst2[3])