# 집합의 포함 여부 확인
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}

print(B.issubset(A))  # True (B는 A의 부분집합인지 확인)
print(A.issuperset(B))  # True (A는 B를 포함하는 집합인지 확인)
