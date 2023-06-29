#if~elif~else

val1 = 50
if val1 <= 100:
    print('if내부')
    if val1 >= 0:
        print('정상')
else:
    print('범위를 벗어남')

val1 = 50
if val1 <= 100 and val1 >= 0:
    print('if내부')
    if val1 >= 0:
        print('정상')
else:
    print('범위를 벗어남')

val1 = 50
if 0 <= val1 <= 100:
    print('if내부')
    if val1 >= 0:
        print('정상')
else:
    print('범위를 벗어남')
