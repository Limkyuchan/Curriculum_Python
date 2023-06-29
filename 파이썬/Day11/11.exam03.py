
# < 딕셔너리 >
# 딕셔너리는 키(key)와 값(value) 쌍을 저장하는 가변(mutable) 데이터 구조
# 딕셔너리는 중괄호 { }를 사용하여 표현
# 키와 값은 콜론: 으로 구분하고 쌍들은 쉼표, 로 구분

# 딕셔너리 생성 및 초기화
empty_dict = {}     # dict() 도 가능
person = {
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}    # 키와 값 쌍을 가진 딕셔너리 생성


# 딕셔너리에서 키를 사용하여 값에 접근하기
person = {
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}   
print(person["name"])   # -> "John"
print(person["age"])    # -> 30
print(person.__getitem__('city'))   # -> "New York"


# 딕셔너리에 새로운 키-값 쌍 추가 및 제거하기
person = {
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}   
person["country"] = "USA"   # 새로운 키-값 쌍 추가
person.__setitem__('address', 'Seoul')

del person["age"]           # "age" 키와 그에 해당하는 값을 제거
person.__delitem__('city')  # "city" 키와 그에 해당하는 값을 제거



# 딕셔너리의 키, 값, 키-값 쌍 가져오기
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

keys = person.keys()  # 키 목록 가져오기
print(keys)  # dict_keys(['name', 'age', 'city'])
print(type(keys))
for key in keys:
    print(f'{key}:{person[key]}')
print()

values = person.values()  # 값 목록 가져오기
print(values)  # dict_values(['John', 30, 'New York'])
print(type(values))
for value in values:
    print(value)
print()

items = person.items()  # 키-값 쌍 가져오기
print(items)  # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
print(type(items))
for k, v in items:
    print(f'{k}:{v}')
print()

for k, v in person.items():
    print(f'{k}:{v}')




# 딕셔너리를 사용하여 여러 학생들의 과목별 성적을 저장하고, 
# 각 학생의 평균 성적을 계산하는 프로그램

# 학생들의 과목별 성적 딕셔너리
grades = {
    "Alice": {"math": 90, "history": 80, "chemistry": 85},
    "Bob": {"math": 78, "history": 92, "chemistry": 89},
    "Charlie": {"math": 85, "history": 85, "chemistry": 95},
    "David": {"math": 92, "history": 88, "chemistry": 75}
}

# 각 학생의 평균 성적을 저장할 딕셔너리
average_grades = {}

# 평균 성적 계산
for student, subjects in grades.items():
    total_score = 0
    subject_count = 0
    for score in subjects.values():
        total_score += score
        subject_count += 1
    average_grades[student] = total_score / subject_count

# 결과 출력
for student, average_grade in average_grades.items():
    print(f"{student}'s average grade is {average_grade:.2f}")
