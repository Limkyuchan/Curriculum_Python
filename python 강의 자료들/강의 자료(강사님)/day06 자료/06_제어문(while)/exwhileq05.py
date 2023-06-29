rice = 80 * 100 * 100
mouse = 2
days = 0

while rice > 0:
    rice -= mouse * 20
    days += 1
    #print(f"{days}일-{mouse}마리가 {mouse * 20}먹음. 창고의 쌀{rice}")
    if days % 10 == 0:
        mouse *= 2

print(f"{days}일이 지나면 창고의 쌀이 모두 쥐의 먹이가 됩니다.")
print(f"현재 창고에 있는 쥐의 수는 {mouse}마리입니다.")