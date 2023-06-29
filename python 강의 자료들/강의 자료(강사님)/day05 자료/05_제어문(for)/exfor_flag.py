line = input('라인 수 입력(홀수):')
if line.isdigit():
    line = int(line)
    flag = True
    star = 1
    space = line // 2
    for i in range(0, line):
        for sp in range(0, space):
            print(' ', end='')
        for st in range(0, star):
            print('*', end='')
        print()
        if i == line // 2:
            flag = not flag
        if flag:
            star += 2
            space -=1
        else:
            star -= 2
            space += 1
else:
    print('숫자만 입력하세요.')

