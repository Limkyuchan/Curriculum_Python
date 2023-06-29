# Properties 파일을 이용한 파일 입출력 예제
"""
Properties 파일은 키와 값으로 이루어진 텍스트 파일
주로 프로그램 설정 정보나 메시지 등을 저장하기 위해 사용
파이썬에서는 Properties 파일을 다루기 위한 모듈인 configparser가 제공됨
"""
import configparser

data = {
    "name": "Bob",
    "age": 25,
    "favorite_foods": ["hamburger", "fries"]
}

config = configparser.ConfigParser()
config['PERSON'] = data

with open('example2.properties', 'w') as f:
    config.write(f)

