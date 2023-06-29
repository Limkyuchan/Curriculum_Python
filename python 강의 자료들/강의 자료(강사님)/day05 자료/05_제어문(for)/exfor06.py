innerForData = ''
for i in range(0, 3):
    for j in range(0, 4):
        innerForData += str(i+j) + ' '
    print(f'i={i}, i+j={innerForData}')
    innerForData = ''