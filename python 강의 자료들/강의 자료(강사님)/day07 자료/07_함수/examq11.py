#파일의 용량(byte)을 매개변수로 입력 받아 bit단위로 반환하는 함수 정의
#파일의 용량을 입력할 때 단위도 입력한다.(G, M, K)
#ex) byteToBit(32,’G’);
#    byteToBit(64,’M’);

# (val * 8) * 1024 * 1024 * 1024 
# (val * 8) * 1024 ** 3

def mypow(x, y):
    return x ** y

def byteToBit(val, unit):
    b = val * 8
    ret = ''
    if unit == 'B':     ret = b
    elif unit == 'K':   ret = b * 1024
    elif unit == 'M':   ret = b * mypow(1024, 2)
    elif unit == 'G':   ret = b * pow(1024, 3) # 파이썬 내장 함수
    else:               ret = '잘못된단위'
    return ret

print( byteToBit(1, 'B') )
print( byteToBit(1, 'K') )
print( byteToBit(1, 'M') )
print( byteToBit(1, 'G') )
print( byteToBit(1, 'A') )