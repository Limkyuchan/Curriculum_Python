num = int(input('수를 입력하세요'))

outputData = ''
for i in range(0, num):
    outputData += str((i+1)*7)+' '
    
print('출력 : ',outputData)
