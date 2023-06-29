# 리스트 확장
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(id(list1))
list1.extend(list2)
print(list1)  # [1, 2, 3, 4, 5, 6]
print(id(list1))

list3 = [1, 2, 3]
list4 = [4, 5, 6]
print(id(list3))
#list3 = list3 + list4
list3 += list4
print(list3)  # [1, 2, 3, 4, 5, 6]
print(id(list3))

