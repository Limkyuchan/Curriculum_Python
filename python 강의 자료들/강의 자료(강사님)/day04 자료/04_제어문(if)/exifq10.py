jumin = int(input('주민번호 7자리를 입력하세요?'))
year = int(jumin/100000)
gender = jumin%10
	
age = 116 - year +1
adult=''
if age>=100:    age -= 100
if age<20:      adult='미'
if gender %2 == 1:  sex='남성'
else :              sex='여성'

print('당신은 {age} {gender}이며 {adult}성년입니다.'.format(age=age, gender=sex, adult=adult))
