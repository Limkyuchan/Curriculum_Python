with open('test.txt', 'w') as file:
    data = '출력 데이터'
    file.write(data)
    print(data, end='')

# file.write('추가 데이터') # ValueError: I/O operation on closed file.