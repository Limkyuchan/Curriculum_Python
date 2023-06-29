blockData = ''
for i in range(0, 3):
    for j in range(0, 4):
        if j%2 == 0:        
            starData = '★'
        else:        
            starData = '☆'
        blockData += starData
    print(f'i={i}, j={blockData}')
    blockData = ''


    