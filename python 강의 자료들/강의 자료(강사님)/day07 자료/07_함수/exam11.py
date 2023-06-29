a = 1
def variableTest(a): #a는 함수의 지역변수
    global a #함수 내부에 동일한 이름의 변수가 있으면 에러
    a = a + 1
    print('variableTest:', a)

print('a:', a)
variableTest(a)
print('a:', a)
variableTest(a)
print('a:', a)


