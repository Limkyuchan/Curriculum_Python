
# # 비교 연산자

# # Q1. 세 수를 입력 받아 합계와 평균을 구하시오. (단, 소수점 2자리까지만 출력)
# #    입력 : 17 26 49        결과 : 합 = 92, 평균 = 30.67

# num1 = int(input("첫 번째 수 입력: "))
# num2 = int(input("두 번째 수 입력: "))
# num3 = int(input("세 번째 수 입력: "))

# total = num1 + num2 + num3
# avg = (num1 + num2 + num3) / 3

# print(f"결과: 합 = {total}, 평균 = {round(avg, 2)}")



# # Q2. 삼각형의 두 각을 입력 받아 나머지 하나의 각을 구하시오.
# #    입력 : 40 80           출력 : 나머지 각은 60도이다.

# a = int(input("각도 입력: "))
# b = int(input("각도 입력: "))

# print(f"출력: 나머지 각은 {180 - (a+b)}도 이다.")



# # Q3. 총 소요시간을 구하여라. 하나의 역을 이동하는데 걸리는 시간은 3분이다.
# #     역의 수를 입력하여 총 소요시간을 계산하시오. (단, 소요시간은 시간과 분으로 처리)
# #    입력 : 정거장 수 27                결과 : 총 소요시간은 1시간 21분 입니다.

# sta = int(input("정거장 수를 입력하시오: "))
# time = sta * 3

# print(f"총 소요시간은 {time//60}시간 {time%60}분 입니다.")



# # Q4. 평면 도형의 꼭지점 개수를 입력하면 입체 도형으로 확장했을 때의
# #     꼭지점, 선, 면의 개수를 구하는 프로그램 작성.
# #    입력 : 꼭지점의 개수 3             결과 : 꼭지점 (6) , 선 (9), 면 (5)

# pi = int(input("꼭지점의 개수 입력: "))

# print(f"꼭지점({pi*2}), 선({pi*3}), 면({pi+2})")



# # Q5. 태어난 년도를 입력 받아 90년대 태어난 사람이면 true를 그 이외에는 false가 나오도록 작성.
# #    입력 : 태어난 년도 입력 91         출력 : True

# year = int(input("태어난 년도 입력: "))

# print(90 <= year < 100)



# # Q6. 파이썬의 영어 철자를 입력하여 맞으면 True를 틀리면 False를 출력하시오.
# #     (단, 소문자일 경우만 처리하시오)

# eng = input("파이썬 영어 철자를 입력: ")

# print(eng == "python")



# # Q7. 두 수를 입력 받아 첫 번째 수가 두 번째 수의 배수이면 true를 아니면 false를 출력
# #    입력 : 첫 번째 수 8  두 번째 수 2            출력 : True

# num1 = int(input("첫 번째 수 입력: "))
# num2 = int(input("두 번째 수 입력: "))

# print(num1 % num2 == 0)



# # Q8. 하나의 수를 입력 받아 12의 약수이면 true를 거짓이면 false를 출력
# #    입력 : 수 입력 5             출력 : False

# num = int(input("수 입력: "))

# print(12 % num == 0)



# # Q9. 두 수를 입력 받아 첫 번째 수가 두 번째 수의 제곱근이면 true를 아니면 false를 출력
# #    입력 : 첫 번째 수 입력 2  두 번째 수 입력  4        출력 : True

# num1 = int(input("첫 번째 수 입력: "))
# num2 = int(input("두 번째 수 입력: "))

# print(num1**2 == num2)



