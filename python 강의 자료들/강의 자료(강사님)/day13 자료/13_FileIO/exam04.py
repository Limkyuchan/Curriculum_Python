file = open('test.txt', 'r')

while True:
    readData = file.readline()
    if not readData:
        break
    print(readData, end='')

file.close()