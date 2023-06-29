# 딕셔너리에서 값에 접근하기 (키를 사용한 인덱싱)
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person["name"])  # "John"
print(person["age"])  # 30
print(person.__getitem__('city'))
# print(person.__getitem__('address'))  # KeyError
# print(person["addr"])                 # KeyError