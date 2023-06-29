file = open('test.txt', 'a')

for i in range(1, 11):
    data = f"{i}추가 출력.\n"
    file.write(data)
    print(data, end='')

file.close()