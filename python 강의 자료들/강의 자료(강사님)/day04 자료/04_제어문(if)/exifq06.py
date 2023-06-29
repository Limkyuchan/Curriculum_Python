floor = int(input('현재 있는 층수를 입력하세요?'))
aElevator = 5
bElevator = 7

aDistance = aElevator - floor
bDistance = bElevator - floor
if aDistance < 0:
	aDistance *= -1
if bDistance < 0:
	bDistance *= -1
if aDistance > bDistance:
    result = 'b 엘리베이터가 {0}층에서 움직입니다.'.format(bElevator)
else:
    result = 'a 엘리베이터가 {0}층에서 움직입니다.'.format(aElevator)
print(result)
