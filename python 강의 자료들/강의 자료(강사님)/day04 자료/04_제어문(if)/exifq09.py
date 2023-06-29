weight = int(input('몸무게를 입력하세요?'))
pound = 2.204623 #0.453592
poundWeight = weight * pound
	
if poundWeight<125:     weightClass = 'fly'
elif poundWeight<135:   weightClass = 'bantam'
elif poundWeight<145:   weightClass = 'feather'
elif poundWeight<155:   weightClass = 'light'
elif poundWeight<170:   weightClass = 'welter'
elif poundWeight<185:   weightClass = 'middle'
elif poundWeight<205:   weightClass = 'light heavy'
else:                   weightClass = 'heavy'
	
print('당신은 {0}급이며 체중은 {1:.4f}파운드입니다.'.format(weightClass, poundWeight))
