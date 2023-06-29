a, b, c = input('입력:').split()
total = int(a) + int(b) + int(c)
avg = total/3
print('결과: 합={0}, 평균={1:.2f}'.format(total, avg))