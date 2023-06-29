limit = 600 #kg
item1 = float(input("첫 번째 물건의 무게(kg):"))
item2 = float(input("두 번째 물건의 무게(kg):"))

free_weight = limit - (item1 + item2)
print(f'남은 여유 무게: {free_weight}/{limit:0.1f}kg')
