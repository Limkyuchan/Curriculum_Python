while True:
    data = input('정수를 입력하세요')
    if data.isdigit():
        num = int(data)
        if num%3==0:print('3의 배수')
    elif data == 'q' or data =='Q':
        break
    else:   print('정수를 입력해야 합니다.')
