weight = float(input('몸무게를 입력하세요?'))
height = float(input('키를 입력하세요?'))

standardWeight = (height - 100) * 0.9
weightRate = weight / standardWeight * 100

if weightRate < 80:
	print('저체중 입니다.')
elif weightRate < 90:
	print('경한저체중 입니다.')
elif weightRate < 110:
	print('정상체중 입니다.')
elif weightRate < 120:
	print('과체중 입니다.')
elif weightRate < 130:
	print('경도비만 입니다.')
elif weightRate < 150:
	print('중증도비만 입니다.')
elif weightRate < 200:
	print('고도비만 입니다.')
else:
	print('위험한 비만 입니다.')
