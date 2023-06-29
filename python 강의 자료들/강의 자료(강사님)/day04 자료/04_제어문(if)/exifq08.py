num1 = float(input('점수를 입력하세요?'))
num2 = float(input('점수를 입력하세요?'))
num3 = float(input('점수를 입력하세요?'))
num4 = float(input('점수를 입력하세요?'))
num5 = float(input('점수를 입력하세요?'))

if num1 > num2:     max = num1
else:           	max = num2
if max < num3:  	max = num3
if max < num4:  	max = num4
if max < num5:  	max = num5
if num1 < num2:     min = num1
else:           	min = num2
if min > num3:  	min = num3
if min > num4:  	min = num4
if min > num5:  	min = num5

sum = num1+num2+num3+num4+num5-max-min
avg = sum/3

print('최대값 {max}, 최소값{min}, 합계{sum:.2f}, 평균{avg:.2f}.'.format(
		max=max, min=min, sum=sum, avg=avg))
