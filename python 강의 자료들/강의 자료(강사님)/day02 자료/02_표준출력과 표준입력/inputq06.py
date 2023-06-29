height = float(input('키 입력(cm):'))
weight = float(input('현재 체중 입력(kg):'))

std_weight = (height - 100) * 0.9
obesiti_lv = weight / std_weight * 100

print(f'{height}cm에 대한 표준 체중: {std_weight:0.2f}kg 비만도 {obesiti_lv:0.0f}%')
