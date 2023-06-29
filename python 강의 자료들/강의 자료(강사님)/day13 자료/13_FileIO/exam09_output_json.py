#JSON 파일을 이용한 파일 입출력 예제
"""
JSON(JavaScript Object Notation)은 자바스크립트에서 사용하는 
객체 표현 방법을 기반으로 한 경량 데이터 교환 형식
JSON은 텍스트 형식으로 되어 있어 사람이 쉽게 읽고 쓸 수 있으면서 
기계가 쉽게 분석하고 생성할 수 있음
파이썬에서는 JSON을 다루기 위한 모듈인 json이 제공됨
"""
import json

data = {
    "name": "Bob",
    "age": 25,
    "favorite_foods": ["hamburger", "fries"]
}

with open('example2.json', 'w') as f:
    json.dump(data, f)
