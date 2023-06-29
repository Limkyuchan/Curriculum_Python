num_grains = 1 
total_grains = num_grains 

for i in range(1, 64):
    num_grains *= 2
    total_grains += num_grains

print(f"발명가가 요구한 밀알의 총 개수는 {total_grains}개입니다.")
