val = input('값 입력:')
if val == '':
    val = 0
else:
    val = int(val)

if val == 0:
    print('입력오류!', val)
else:
    print('정상입력!', val)