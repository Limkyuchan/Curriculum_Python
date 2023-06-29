"""
딕셔너리(Dictionary)는 키(key)와 값(value) 쌍을 저장하는 
가변(mutable) 데이터 구조
딕셔너리는 중괄호({})를 사용하여 표현
키와 값은 콜론(:)으로 구분하고 쌍들은 쉼표(,)로 구분
"""
# 딕셔너리 생성 및 초기화
empty_dict = dict() #{}  # 빈 딕셔너리 생성 dict()
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}  # 키와 값 쌍을 가진 딕셔너리 생성

print(empty_dict)
print(person)