blockData = ''
for i in range(0, 3):
    for j in range(0, 4):
        if i%2 == 0:
            blockData += '★'
        else:
            blockData += '☆'
    print(f'i={i}, j={blockData}')
    blockData = ''


    