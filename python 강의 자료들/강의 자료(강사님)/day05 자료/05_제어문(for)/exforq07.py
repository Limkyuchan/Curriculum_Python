num = int(input('수를 입력하세요?'))
outputData = ''

for i in range(num*2+1):
    if i%num==0:outputBlock='■'
    else:       outputBlock='□'
    for j in range(5):
        outputData += outputBlock
    print(outputData)
    outputData=''
