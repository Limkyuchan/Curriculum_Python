# 딕셔너리에 새로운 키-값 쌍 추가하기
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
person["country"] = "USA"  # 새로운 키-값 쌍 추가
person.__setitem__('address', 'Seoul')
print(person)  # {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}
