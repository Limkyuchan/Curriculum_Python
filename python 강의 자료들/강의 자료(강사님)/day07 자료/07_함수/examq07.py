#표준체중 반환 함수
def stdWeight(height):
    return (height - 100) * 0.9

#비만도 반환 함수
def obesityRate(cur_weight, height):
    return cur_weight / stdWeight(height) * 100

#비만도 판정 함수
def obesityResult(cur_weight, height):
    obesity = obesityRate(cur_weight, height)
    if obesity >= 200:       ret='위험한 비만'
    elif obesity >= 150:     ret='고도 비만'
    elif obesity >= 130:     ret='중증도 비만'
    elif obesity >= 120:     ret='경도 비만'
    elif obesity >= 110:     ret='과체중'
    elif obesity >= 90:      ret='정상체중'
    elif obesity >= 80:      ret='경도 저체중'
    else:                    ret='저체중'
    return ret

height1, weight1 = 164.9, 74.8
obesity1 = round(obesityRate(weight1, height1), 2)
ret1 = obesityResult(weight1, height1)
print('키:{0}cm, 몸무게:{1}kg, 비만도:{2}%, 결과:{3}'
      .format(height1, weight1, obesity1, ret1))





height1, weight1 = 164.9, 74.8
height2, weight2 = 168.8, 78.3
height3, weight3 = 154.3, 45.7

obesity1 = round(obesityRate(weight1, height1), 2)
obesity2 = round(obesityRate(weight2, height2), 2)
obesity3 = round(obesityRate(weight3, height3), 2)

ret1 = obesityResult(weight1, height1)
ret2 = obesityResult(weight2, height2)
ret3 = obesityResult(weight3, height3)

print('키:{0}cm, 몸무게:{1}kg, 비만도:{2}%, 결과:{3}'
      .format(height1, weight1, obesity1, ret1))
print('키:{0}cm, 몸무게:{1}kg, 비만도:{2}%, 결과:{3}'
      .format(height2, weight2, obesity2, ret2))
print('키:{0}cm, 몸무게:{1}kg, 비만도:{2}%, 결과:{3}'
      .format(height3, weight3, obesity3, ret3))

