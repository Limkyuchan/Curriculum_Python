class MyError(Exception):
    pass

def valuecheck(n):
    if not 0 <= n <= 100:
        raise MyError('범위에러')

valuecheck(50)
valuecheck(12)
try:
    valuecheck(-1) # 예외처리
except MyError as msg:
    print('예외:', msg)
valuecheck(77)
valuecheck(101) # __main__.MyError: 범위에러 예외발생