#임의의 개수로 실수를 입력 받아 
# 최소값과 최대값을 제외한 나머지 점수들의 합계를 
# 반환하는 함수를 정의(가변인자 활용)
def middleSum(*args):
    max_val, min_val, total = 0,0,0
    size = len(args)
    if size != 0:
        min_val = args[0]
    else:
        return -1
    for i in range(size):
        if args[i] >= max_val:      max_val = args[i]
        elif args[i] <= min_val:    min_val = args[i]
        total += args[i]

    result = total - (min_val + max_val)
    return result

#그냥 호출 테스트
print( middleSum() )
print( middleSum(1,2,3,4,5,6) )
print( middleSum(0,1,2,3,4,5,6,7,8,9,10,11) )

#리스트 전달(unpack)
data = [1, 2, 3, 4, 5, 6]
print( middleSum(*data) )

#입력받은 문자열을 리스트로 만들어 전달(unpack)
data = input('숫자만 입력(빈칸으로 구분):').split()
i = 0
while i < len(data):
    data[i] = int(data[i])
    i += 1
print( middleSum(*data) )

