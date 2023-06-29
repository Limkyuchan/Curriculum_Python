
# # 함수

# # Q1. 숫자를 입력 받아 음수를 판별하는 함수 정의

# def 음수(x):
#     if x < 0:
#         return "음수"
#     return "양수"

# num = int(input("수 입력: "))
# print(f"{num}는(은) {음수(num)}입니다")


# # Q2. 태어난 년도를 2자리로 입력하여 나이를 구하는 함수 정의

# def 나이(x):
#     if x <= 23:
#         return 23 - x + 1
#     elif 23 < x < 100: 
#         return 123 - x + 1
    
# year = int(input("태어난 년도(2자리) 입력: "))
# print(f"나이는 {나이(year)}살")


# # Q3. 태어난 년도를 2자리 혹은 4자리로 입력받아 우리나라 나이를 반환하는 함수 정의

# def 나이2(x):
#     if 0 <= x < 100:
#         if x <= 23:
#             return 23 - x + 1
#         else:
#             return 123 - x + 1
#     else:
#         return 2023 - x + 1
    
# year2 = int(input("태어난 년도 입력(2자리 or 4자리): "))
# print(f"나이는 {나이2(year2)}살")


# # Q4. 숫자를 입력 받아 절대값을 반환하는 함수 정의

# def 절대값(x):
#     if x < 0:
#         return -x
#     else:
#         return x
    
# n = int(input("숫자 입력: "))
# print(f"{n}의 절대값은 {절대값(n)}")


# # Q5. 1부터 입력한 수 까지의 합을 반환하는 함수정의

# def 합(x):
#     hap = 0
#     for i in range(1,x+1):
#         hap += i
#     return hap

# su = int(input("수 입력: "))
# print(f"1부터 {su}까지의 합은 {합(su)}")


# # Q6. 수를 입력 받아 1부터 입력한 수 사이의 2의 배수들의 합을 반환해주는 함수 정의

# def 이배수(x):
#     hap = 0
#     for i in range(1,x):
#         if i % 2 == 0:
#             hap += i
#     return hap

# sut = int(input("수 입력: "))
# print(f"1부터 {sut}사이 2의 배수들의 합은 {이배수(sut)}")


# # Q7. 표준체중을 반환하는 함수를 정의하고, 비만도를 반환하는 함수를 정의

# def 표준체중(x):
#     return round((x - 100) * 0.9, 2)
    
# def 비만도(y):
#     y = round((weight / 표준체중(height)) * 100, 2)
    
#     if y < 80:
#         return f"{y}, 저체중"
#     elif y < 90:
#         return f"{y}, 경한 저체중"
#     elif y < 110:
#         return f"{y}, 정상체중"
#     elif y < 120:
#         return f"{y}, 과체중"
#     elif y < 130:
#         return f"{y}, 경도비만"
#     elif y < 150:
#         return f"{y}, 중증도비만"
#     elif y < 200:
#         return f"{y}, 고도비만"
#     else:
#         return f"{y}, 위험한 비만"

# height = float(input("현재 신장 입력(cm): "))
# weight = float(input("현재 체중 입력(kg): "))

# print(f"표준체중: {표준체중(height)}")
# print(f"비만도는 {비만도(weight)}")