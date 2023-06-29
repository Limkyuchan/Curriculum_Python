a = 1
def variableTest():
    global a #외부의 함수를 내부에서 사용하도록 선언
    a = a + 1
    print('variableTest:', a)

print('a:', a)
variableTest()
print('a:', a)
variableTest()
print('a:', a)

