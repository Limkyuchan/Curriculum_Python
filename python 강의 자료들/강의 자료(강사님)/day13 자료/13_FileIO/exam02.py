file = open('test.txt', 'w')

for i in range(1, 11):
    data = f"{i}출력.\n"
    file.write(data)
    print(data, end='')

file.close()