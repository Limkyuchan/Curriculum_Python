blockData = ''
for i in range(0, 3):
    if i%2 == 0:        
        starData = '★'
    else:        
        starData = '☆'
    for j in range(0, 4):
        blockData += starData
    print(f'i={i}, j={blockData}')
    blockData = ''


    