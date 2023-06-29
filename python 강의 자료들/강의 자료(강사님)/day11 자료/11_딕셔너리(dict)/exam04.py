# 딕셔너리에서 키-값 쌍 제거하기
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
del person["age"]  # "age" 키와 그에 해당하는 값을 제거
person.__delitem__('city')
print(person)  # {'name': 'John'}
