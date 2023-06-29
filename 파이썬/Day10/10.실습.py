
# 리스트(list)

# Q1. 5명의 이름과 나이를 저장하고 출력하는 프로그램 작성. 한 번에 다섯 명의 정보를 저장하고 출력한다.

li = []
for i in range(1,6):
    print(f"{i}번째 정보 입력")
    name = input("이름: ")
    age = int(input("나이: "))
    li.append([name, age])

for i in range(1,6):
    print(f"{i}정보")
    print(f"이름: {li[i-1][0]}, 나이: {li[i-1][1]}세")

# 나이 순으로 정렬되어 출력되도록 기능 추가
li = sorted(li, key = lambda x: x[1])
print(li)





# Q2. 주민번호 검증하기

num = []
num2 = input("주민번호 13자리 입력: ")

for i in range(13):
    num.append(num2[i])                 # 문자열로 안받고 리스트로 (문자열은 num2 형식 그대로)

hap = 0
su = 2
for i in range(12):
    if i <= 7:
        hap += int(num[i])*su
    else:
        hap += int(num[i])*(su-8)
    su += 1

result_num = (11 - (hap % 11)) % 10
print(f"검증번호: {result_num}, 주민번호 끝자리: {num[-1]}", end = "\t\t")

if int(num[-1]) == result_num:
    print("주민번호 정상!")
else:
    print("주민번호 오류!")





# Q3. 주민번호 랜덤으로 생성 후 검증번호 확인
from random import randint

num = ""
for i in range(8):
    if i == 0:
        year = randint(0,99)
        if year < 10:
            year = "0" + str(year)
            num += year
        else:
            num += str(year)
    elif i == 1:
        month = randint(1,12)
        if month < 10:
            month = "0" + str(month)
            num += month
        else:
            num += str(month)
    elif i == 2:
        day = randint(1,31)
        if day < 10:
            day = "0" + str(day)
            num += day
        else:
            num += str(day)
    elif i == 3:
        mw = randint(1,4)
        num += str(mw)
    elif i == 4:
        d = randint(0,9)
        num += str(d)
    elif i == 5:
        gu = randint(0,99)
        if gu < 10:
            gu = "0" + str(gu)
            num += gu
        else:
            num += str(gu)
    elif i == 6:
        dong = randint(0,99)
        if dong < 10:
            dong = "0" + str(dong)
            num += dong
        else:
            num += str(dong)
    else:
        la = randint(0,9)
        num += str(la)

print(f"랜덤 생성된 주민번호: {num}")
print()

hap  = 0
su = 2
for i in range(12):
    if i < 8:
        hap += int(num[i]) * su
    else:
        hap += int(num[i]) * (su-8)
    su += 1

result_num = (11 - (hap%11)) % 10

print(f"검증번호: {result_num},  주민번호 끝 자리: {num[-1]}", end = "   ")

if int(num[-1]) == result_num:
    print("주민번호 정상")
else:
    print("주민번호 오류!")
print()





# Q4. [알고리즘] 어떤 자연수 n이 있을때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의
#     예를 들어 d(91) = 9 + 1 + 91 = 101 과 같은 식이 있을때 n을 d(n)의 제너레이터라고 함
#     101의 제너레이터는 91 뿐 아니라 100(d(100) = 1 + 0 + 0 + 100 = 101)도 있다.
#     어떤 숫자들은 제너레이터를 가지고 있지 않다.
#     이런 숫자를 인도의 수학자 kaprekar가 셀프 넘버라 이름 붙였다.
#     예를 들어 1,3,5,7,9,20,31,... 은 셀프 넘버 들이다.
#     [문제] 1 이상이고 5000보다 작은 작은 모든 셀프 넘버들의 합을 구하라.

# 1)
generator = []
for i in range(1,5000):
    if i < 10:
        generator.append(i%10 + i)
    elif 10 <= i < 100:
        generator.append(i//10 + i%10 + i)
    elif 100 <= i < 1000:
        generator.append(i//100 + i//10%10 + i%10 + i)
    else:
        generator.append(i//1000 + i//100%10 + i%100//10 + i%10 + i)

number = []
for i in range(1,5000):
    if i not in generator:
        number.append(i)

print(f"셀프 넘버들의 합: {sum(number)}")


# 2) 함수 사용
# d(n) 함수 구현
def d(n):
    result = n
    for i in str(n):
        result += int(i)
    return result

# 제너레이터 값을 제거 (셀프넘버 구하기)
num = list(range(1,5000))
for i in range(1,5000):
    if d(i) in num:
        num.remove(d(i))

# 셀프넘버들의 합
total = 0
for i in num:
    total += i
print(f"셀프 넘버들의 합: {total}")





# Q5. 반과 전교학생의 성적처리 프로그램
#     실행 후 과목 수를 입력 받고 그 수만큼 과목명을 리스트로 생성한다.
#     ex) 과목수: 2     과목명1: 국어     과목명2: 영어

# 과목수 = int(input("과목 수 입력: "))

class_1 = []
class_2 = []

total_class = int(input("총 몇반? "))
for i in range(total_class):
    if i == 0:
        su = int(input(f"{i}반의 인원수: "))
        for j in range(su):
            print(f"{i}번째 반의 {j}번째 사람 이름: ", end = "")
            name = input("")
            kor = int(input("국어 점수: "))
            eng = int(input("영어 점수: "))
            class_1.append([name, kor, eng])
    elif i == 1:
        su = int(input(f"{i}반의 인원수: "))
        for j in range(su):
            print(f"{i}번째 반의 {j}번째 사람 이름: ", end = "")
            name = input("")
            kor = int(input("국어 점수: "))
            eng = int(input("영어 점수: "))
            class_2.append([name, kor, eng])
 
total_score1 = [[class_1[0][1]+class_1[0][2]] + [class_1[1][1]+class_1[1][2]]]
total_score2 = [[class_2[0][1]+class_2[0][2]] + [class_2[1][1]+class_2[1][2]] + [class_2[2][1]+class_2[2][2]]]


print("이름 \t 국어 \t 영어 \t 총점 \t 반석차 \t 전교석차 \t 평균")

