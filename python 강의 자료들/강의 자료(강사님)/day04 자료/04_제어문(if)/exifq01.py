num = int(input('숫자를 입력하세요'))
minusStr=''
if num<0:
    minusStr='음수이며 '

print("{0}{1}을(를) 입력하였습니다.".format(minusStr, num))

