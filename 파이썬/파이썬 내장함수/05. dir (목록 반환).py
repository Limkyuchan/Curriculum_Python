
# < dir >
# 객체 자체가 가지는 변수와 함수 목록을 반환

n = dir([1,2,3])
print(n)
print()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printxy(self):
        print(f'[{self.x}, {self.y}]')

pos = Point(10, 20)
n = dir(pos)
print(n)