# XML 파일을 이용한 파일 입출력 예제
"""
XML(Extensible Markup Language)은 데이터를 저장하고 전송하기 위한 마크업 언어
데이터를 계층적인 구조로 표현하며, 태그와 속성을 이용하여 데이터를 기술
파이썬에서는 XML을 다루기 위한 모듈인 xml.etree.ElementTree가 제공됨
"""
import xml.etree.ElementTree as ET

tree = ET.parse('example.xml')
root = tree.getroot()

data = {}
data['name'] = root.find('name').text
data['age'] = int(root.find('age').text)
data['favorite_foods'] = [food.text for food in root.find('favorite_foods')]

print(data)
print(type(data))

