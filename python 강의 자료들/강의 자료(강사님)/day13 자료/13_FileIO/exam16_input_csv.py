# CSV 파일을 이용한 파일 입출력 예제
"""
CSV 파일은 쉼표(,)로 구분된 텍스트 파일로, 
행과 열로 이루어진 2차원 데이터를 저장하기 위해 사용
파이썬에서는 CSV 파일을 다루기 위한 모듈인 csv가 제공됨
"""
import csv

with open('example.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [dict(zip(header, row)) for row in reader]

print(data)



