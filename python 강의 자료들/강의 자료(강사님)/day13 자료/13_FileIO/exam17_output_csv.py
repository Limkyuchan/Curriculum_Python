# CSV 파일을 이용한 파일 입출력 예제
"""
CSV 파일은 쉼표(,)로 구분된 텍스트 파일로, 행과 열로 이루어진 2차원 데이터를 저장하기 위해 사용됩니다. 파이썬에서는 CSV 파일을 다루기 위한 모듈인 csv가 제공됩"""
import csv

data = [
    {"name": "Alice", "age": 30, "favorite_foods": ["pizza", "pasta"]},
    {"name": "Bob", "age": 25, "favorite_foods": ["hamburger", "fries"]},
    {"name": "Cal", "age": 40, "favorite_foods": ["bulgogi", "kimpab"]}
]

with open('example2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "favorite_foods"])
    for row in data:
        writer.writerow([row["name"], row["age"], ", ".join(row["favorite_foods"])])


