
# < enumerate >
# 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을
# 포함하는 enumerate 객체를 반환하는 함수 (for문과 함께 활용)

lst = ['body', 'foo', 'bar']
for i, name in enumerate(lst):
    print(i, name)
print()

dt = {'body':'A', 'B':'foo', 'bar':'C'}
for i, e in enumerate(dt):
    print(i, e, dt[e])