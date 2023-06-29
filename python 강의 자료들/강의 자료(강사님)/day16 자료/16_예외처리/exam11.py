def valuecheck(n):
    if not 0 <= n <= 100:
        return
    else:
        n * n

valuecheck(50)
valuecheck(12)
valuecheck(-1)
valuecheck(77)
valuecheck(101)