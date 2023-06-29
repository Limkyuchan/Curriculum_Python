# XML 파일을 이용한 파일 입출력 예제
"""
XML(Extensible Markup Language)은 데이터를 저장하고 전송하기 위한 마크업 언어
데이터를 계층적인 구조로 표현하며, 태그와 속성을 이용하여 데이터를 기술
파이썬에서는 XML을 다루기 위한 모듈인 xml.etree.ElementTree가 제공됨
"""
import xml.etree.ElementTree as ET

data = {
    "name": "Bob",
    "age": 25,
    "favorite_foods": ["hamburger", "fries"]
}

root = ET.Element('person')
name = ET.SubElement(root, 'name')
name.text = data['name']
age = ET.SubElement(root, 'age')
age.text = str(data['age'])
favorite_foods = ET.SubElement(root, 'favorite_foods')
for food in data['favorite_foods']:
    ET.SubElement(favorite_foods, 'food').text = food

tree = ET.ElementTree(root)
tree.write('example2.xml', encoding='utf-8', xml_declaration=True)

