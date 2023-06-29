# YAML 파일을 이용한 파일 입출력 예제
"""
YAML(YAML Ain't Markup Language)은 인간이 쉽게 읽고 쓸 수 있는 데이터 직렬화 형식
들여쓰기와 콜론을 이용하여 데이터를 구조화하며, 다양한 데이터 타입을 지원
파이썬에서는 YAML을 다루기 위한 모듈인 PyYAML이 제공됨
모듈 인스톨 필요
    > pip install pyyaml
"""
import yaml

data = {
    "name": "Bob",
    "age": 25,
    "favorite_foods": ["hamburger", "fries"]
}

with open('example2.yml', 'w') as f:
    yaml.safe_dump(data, f)
