
# # 제어문 (조건문(분기문))

# # Q1. 숫자를 입력 받아 절대값을 구하는 프로그램을 작성하시오.
# #     (절대값이란 0을 기준으로 떨어진 거리를 의미한다.)

# num = int(input("숫자 입력: "))

# if num > 0:
#     print(f"절대값은 {num}")
# elif num < 0:
#     print(f"절대값은 {-num}")
# else:
#     print(f"절대값은 {num}")



# # Q2. 유효사거리는 50m이며 사용자의 현재위치와 타겟의 거리를 계산하는 프로그램을 작성하시오.
# #   입력: 사용자의 거리를 입력하세요 80         출력: 최대유효사거리보다 30m 멉니다.
# #   입력: 사용자의 거리를 입력하세요 39         출력: 최대유효사거리보다 11m 가깝습니다.
# #   입력: 사용자의 거리를 입력하세요 50         출력: 최대유효사거리와 정확히 일치합니다.

# far = int(input("사용자의 거리를 입력하세요: "))

# if far > 50:
#     print(f"최대유효사거리보다 {far-50}m 멉니다.")
# elif far < 50:
#     print(f"최대유효사거리보다 {50-far}m 가깝습니다.")
# else:
#     print("최대유효사거리와 정확히 일치합니다.")



# # Q3. 현재 건물에는 2대의 엘리베이터가 있고 A 엘리베이터는 5층에, B 엘리베이터는 7층에 있다.
# #     현재 내가 있는 층수를 눌러 가장 가까운 엘리베이터를 움직일 수 있도록 프로그램을 작성하라.

# my = int(input("현재 내가 있는 층수:  "))

# if my >= 7:
#     print("B 엘리베이터를 이용하세요.")
# elif my <= 5:
#     print("A 엘리베이터를 이용하세요.")
# else:
#     print("A와 B엘리베이터 모두 이용가능합니다.")



# # Q4. 다음 내용을 참고하여 비만도를 측정하는 프로그램을 작성하시오.
# #     표준체중(kg) = (현재신장cm - 100) x 0.9
# #     비만도(%) = (현재체중 / 표준체중) x 100

# height = float(input("현제 키(cm) 입력: "))
# weight = float(input("현재 체중(kg) 입력: "))

# stan_kg = (height - 100) * 0.9
# fit = (weight / stan_kg) * 100
# fit = round(fit, 2)

# if fit >= 200:
#     print(f"비만도는 {fit}(으)로 위험한 비만 입니다.")
# elif 150 <= fit < 200:
#     print(f"비만도는 {fit}(으)로 고도비만 입니다.")
# elif 130 <= fit < 150:
#     print(f"비만도는 {fit}(으)로 중증도비만 입니다.")
# elif 120 <= fit < 130:
#     print(f"비만도는 {fit}(으)로 경도비만 입니다.")
# elif 110 <= fit < 120:
#     print(f"비만도는 {fit}(으)로 과체중 입니다.")
# elif 90 <= fit < 110:
#     print(f"비만도는 {fit}(으)로 정상체중 입니다.")
# elif 80 <= fit < 90:
#     print(f"비만도는 {fit}(으)로 경한저체중 입니다.")
# else:
#     print(f"비만도는 {fit}(으)로 저체중 입니다.")



# # Q5. 5개의 실수를 입력 받아 최소값과 최대값을 제외한 나머지 점수들의 합계와 평균을 구하시오.

# n1 = float(input("점수를 입력하세요(실수): "))
# n2 = float(input("점수를 입력하세요(실수): "))
# n3 = float(input("점수를 입력하세요(실수): "))
# n4 = float(input("점수를 입력하세요(실수): "))
# n5 = float(input("점수를 입력하세요(실수): "))

# score = (n1, n2, n3, n4, n5)
# total = (n1 + n2 + n3 + n4 + n5)

# sum = total - (max(score) + min(score))
# avg = sum / 3

# print(f"합계는 {sum}, 평균은 {avg}")



# # Q6. 몸무게를 kg단위로 입력하면 파운드(lb)단위로 변경하고 다음 체급표에 맞게 체급을 출력하는 프로그램 작성.
# #     1kg (kg)은 2.20462262185 파운드 (lbs)와 같습니다

# weight = int(input("몸무게를 입력하세요(kg): "))

# lb = weight * 2.20462262185
# lb = round(lb, 4)

# if lb < 125:
#     print(f"당신은 fly급이며 체중은 {lb}파운드 입니다.")
# elif lb < 135:
#     print(f"당신은 bantam급이며 체중은 {lb}파운드 입니다.")
# elif lb < 145:
#     print(f"당신은 feather급이며 체중은 {lb}파운드 입니다.")
# elif lb < 155:
#     print(f"당신은 light급이며 체중은 {lb}파운드 입니다.")
# elif lb < 170:
#     print(f"당신은 welter급이며 체중은 {lb}파운드 입니다.")
# elif lb < 185:
#     print(f"당신은 middle급이며 체중은 {lb}파운드 입니다.")
# elif lb < 205:
#     print(f"당신은 light heavy급이며 체중은 {lb}파운드 입니다.")
# elif lb < 265:
#     print(f"당신은 heavy급이며 체중은 {lb}파운드 입니다.")



# # Q7. 주민번호 7자리를 입력 받아 나이와 성별을 구하시오.
# #     9  6(년)  0  8(월)  1  5(일)  2(성별) 
# #   입력: 주민번호 7자리를 입력하세요 0101014       출력: 당신은 16 여성이며 미성년입니다.
# #   입력: 주민번호 7자리를 입력하세요 9608151       출력: 당신은 21 남성이며 성년입니다.

# # 1)
# bir = input("주민번호 7자리를 입력하세요: ")

# na = bir[:2]
# mal = bir[-1]

# na = int(na)
# mal = int(mal)

# if mal == 2 or mal == 4:
#     mal = "여성"
# elif mal == 1 or mal == 3:
#     mal = "남성"

# if na <= 23:
#     if 23 - na >= 20:
#         grade = "성년"
#     else:
#         grade = "미성년"
# else:
#     grade = "성년"

# print(na <= 23 and f"당신은 {23 - na + 1} {mal}이며 {grade}입니다." \
#                or f"당신은 {123 - na + 1} {mal}이며 {grade}입니다.")


# # 2)
# bir = int(input("주민번호 7자리를 입력하세요: "))

# year = bir // 100000
# x = bir % 10

# if x == 1:
#     print(f"당신은 {123-year + 1} 남성이며 성년입니다.")
# elif x == 2:
#     print(f"당신은 {123-year + 1} 여성이며 성년입니다.")
# elif x == 3:
#     if 23 - year >= 20:
#         grade = "성년"
#     else:
#         grade = "미성년"
#     print(f"당신은 {23-year+1} 남성이며 {grade}입니다.")
# elif x == 4:
#     if 23 - year >= 20:
#         grade = "성년"
#     else:
#         grade = "미성년"
#     print(f"당신은 {23-year+1} 여성이며 {grade}입니다.")
# else:
#     print("주민번호 입력 오류!!")