sumValue = 0
cnt = 0
while True:
    data = input('정수를 입력하세요')
    if data.isdigit():
        num = int(data)
        sumValue += num
        cnt += 1
        if num > 9:
            break
