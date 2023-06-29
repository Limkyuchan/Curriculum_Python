weight = float(input('현재 체중 입력(kg):'))
std_weight = float(input('표준 체중 입력(kg):'))
obesiti_lv = weight / std_weight * 100
print(f'비만도: {obesiti_lv:0.0f}%')
