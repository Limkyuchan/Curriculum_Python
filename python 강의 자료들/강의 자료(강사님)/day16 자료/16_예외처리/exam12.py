class MyError(Exception):
    pass

def valuecheck(n):
    if not 0 <= n <= 100:
        raise MyError('범위에러')

valuecheck(50)
valuecheck(12)
valuecheck(-1)
valuecheck(77)
valuecheck(101)