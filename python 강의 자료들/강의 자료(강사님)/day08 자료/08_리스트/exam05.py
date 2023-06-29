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