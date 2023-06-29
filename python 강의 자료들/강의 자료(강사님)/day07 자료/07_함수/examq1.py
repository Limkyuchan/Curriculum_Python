#숫자를 입력받아 음수를 판별하는 함수 정의
'''
n = int(input('수 입력:'))
if n < 0:
    print(True) #print('음수')
else:
    print(False) #print('양수')
'''
#함수로 변경
def minusValue(value):
    ret = False
    if value < 0:
        ret = True #print(True) #print('음수')
    else:
        ret = False #print(False) #print('양수')
    return ret
    
ret = minusValue(-4)
print(ret)