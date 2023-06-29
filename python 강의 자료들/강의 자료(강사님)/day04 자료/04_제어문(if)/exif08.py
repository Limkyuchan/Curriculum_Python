grade = int(input('점수 입력:'))

if grade >= 90:
    result = 'A'
elif grade >= 80:
    result = 'B'
elif grade >= 70:
    result = 'C'
elif grade >= 60:
    result = 'D'
else:
    result = 'F'

print('당신의 학점은 {}입니다.'.format(result))

