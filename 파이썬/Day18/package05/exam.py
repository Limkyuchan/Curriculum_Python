
import sys

# 기본적으로 파이썬에서 Module을 검색하는 방법
# - 모듈 검색 경로를 알고 싶다면 sys.path를 통해 검색


print(sys.path)
"""
[
'C:\\Users\\denni\\OneDrive\\바탕 화면\\퍼블릭 클라우드 서비스를 활용한 파이썬 기반\\python\\파이썬\\Day18\\package05', 
'C:\\Python\\Python311\\python311.zip', 
'C:\\Python\\Python311\\DLLs', 
'C:\\Python\\Python311\\Lib', 
'C:\\Python\\Python311', 
'C:\\Python\\Python311\\Lib\\site-packages'
]

"""

# 경로를 추가로 등록할 수 도 있다.      ex) 추가할 경로: (D:\\my\\) 
# - sys.path.append("추가할 경로")
# - print(sys.path)

