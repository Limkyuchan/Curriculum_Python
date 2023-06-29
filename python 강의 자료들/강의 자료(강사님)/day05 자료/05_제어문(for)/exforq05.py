num = int(input('수를 입력하세요'))

twoData = ''
threeData = ''
for i in range(1, num+1):
    if(i%2==0 and i%3!=0):
        twoData += str(i)+' '
    if(i%2!=0 and i%3==0):
        threeData += str(i)+' '
    
print('2의 배수 : ',twoData)
print('3의 배수 : ',threeData)
