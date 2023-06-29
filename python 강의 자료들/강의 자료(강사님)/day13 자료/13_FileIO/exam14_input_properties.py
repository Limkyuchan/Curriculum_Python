# Properties 파일을 이용한 파일 입출력 예제
"""
Properties 파일은 키와 값으로 이루어진 텍스트 파일
주로 프로그램 설정 정보나 메시지 등을 저장하기 위해 사용
파이썬에서는 Properties 파일을 다루기 위한 모듈인 configparser가 제공됨
"""
import configparser

config = configparser.ConfigParser()
config.read('example.properties')

data = {}
data['name'] = config.get('DEFAULT', 'name')
data['age'] = config.getint('DEFAULT', 'age')
data['favorite_foods'] = config.get('DEFAULT', 'favorite_foods').split(', ')

print(data)


