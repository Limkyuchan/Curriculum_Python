for i in range(0, 5):
    for j in range(0, 5):
        print(f'[{i},{j}]', end='')
    print()

i = 0
while i < 5:
    j = 0
    while j < 5:
        print(f'[{i},{j}]', end='')
        j += 1
    i += 1