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