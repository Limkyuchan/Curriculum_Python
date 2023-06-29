distance = int(input('사용자의 거리를 입력하세요?'))

if distance > 50:
	result = '보다 {0}m 멀리 있습니다.'.format(distance-50)
elif distance < 50:
	result = '보다 {0}m 가까이 있습니다.'.format(50-distance)
else:
	result = '와 정확히 일치합니다.'

print('최대유효사거리{0}'.format(result))
