# 리스트 복사(mutable)
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)  # [1, 2, 3]
print(id(original_list))
print(id(copied_list))
