# 집합 연산
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 합집합
union_set = A | B
print(union_set)  # {1, 2, 3, 4, 5, 6, 7, 8}

# 교집합
intersection_set = A & B
print(intersection_set)  # {4, 5}

# 차집합
difference_set = A - B
print(difference_set)  # {1, 2, 3}

# 대칭차집합
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

symmetric_difference_set = A ^ B
print(symmetric_difference_set)  # {1, 2, 3, 6, 7, 8}
