# 튜플을 사용하여 여러 사람들의 이름, 나이, 성별을 저장한 후, 
# 나이 순으로 정렬하고 결과를 출력하는 프로그램
# 사람들의 이름, 나이, 성별 정보
people = [
    ("Alice", 30, "F"),
    ("Bob", 25, "M"),
    ("Charlie", 35, "M"),
    ("David", 28, "M"),
    ("Eva", 22, "F"),
    ("Frank", 29, "M")
]

# 나이 순으로 정렬
sorted_people = sorted(people, key=lambda x: x[1])

# 결과 출력
for person in sorted_people:
    name, age, gender = person
    print(f"{name} is {age} years old and {gender}.")
