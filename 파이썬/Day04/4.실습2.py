
# # 반복문

# # Q1. 다음과 같이 출력되도록 프로그램을 작성하시오.

# st = input("문자 입력: ")

# for i in range(1,6):
#     print(f"{i}.{st}")



# # Q2. 1부터 입력한 수 까지의 합을 구하는 프로그램을 작성하시오.

# N = int(input("수 입력: "))

# su = 0
# for i in range(1,N+1):
#     su += i
# print(f"1 ~ {N} 합 : {su}")



# # Q3. 숫자를 입력 받아 입력한 수부터 0까지 카운트 다운하는 프로그램을 작성하시오.

# # 1)
# num = int(input("숫자 입력: "))

# for i in range(num, -1, -1):
#     print(i)

# # 2)
# num = int(input("숫자 입력: "))

# for i in range(num + 1):
#     print(num)
#     num -= 1



# # Q4. 10 이하의 정수를 5개 입력 받아 짝수이면 출력.

# # 1)
# n1 = ""
# for i in range(5):
#     n = int(input("10 이하 정수 입력: "))
    
#     if n % 2 == 0:
#         n1 += (str(n) + " ")
# print(f"짝수는 {n1}")

# # 2)
# for i in range(5):
#     n = int(input("수 입력: "))
    
#     if n % 2 == 0:
#         print(n, end = " ")
# print()

# # Q5. 수를 입력 받아 1부터 입력한 수 사이의 2의 배수를 출력.

# su = int(input("수 입력: "))

# print(f"1부터 {su}사이의 2의 배수는", end = " ")
# for i in range(2,su):
#     if i % 2 == 0:
#         print(i,  end = " ")
# print()


# # Q6. 수를 입력 받아 1부터 입력한 수 사이의 3의 배수를 출력.

# su1 = int(input("수 입력: "))

# print(f"1부터 {su1}사이의 3의 배수는", end = " ")
# for i in range(2,su1):
#     if i % 3 == 0:
#         print(i, end = " ")
# print()


# # Q7. 수를 입력 받아 1부터 입력한 수 사이의 2의 배수와 3의 배수를 출력.

# su2 = int(input("수 입력: "))

# print(f"1부터 {su2}사이의 2의 배수와 3의 배수는", end = " ")
# for i in range(2,su2):
#     if i % 2 == 0 or i % 3 == 0:
#         print(i,  end = " ")
# print()


# # Q8. 수를 입력 받아 1부터 입력한 수 사이의 2와 4의 공배수를 출력.

# su3 = int(input("수 입력: "))

# print(f"1부터 {su3}사이의 2와 4의 공배수는", end = " ")
# for i in range(2,su3):
#     if i % 2 == 0 and i % 4 == 0:
#         print(i, end = " ")
# print()


# # Q9. 5개의 점수를 입력 받아 최대값을 출력.

# # 1)
# max = 0

# for i in range(5):
#     score = int(input("점수 입력: "))

#     if score > max:
#         max = score
# print(f"최대값은 {max}")

# # 2)
# num1, num2, num3, num4, num5 = map(int,input("점수 5개 입력: ").split())

# score = (num1, num2, num3, num4, num5)
# max = 0

# for score in score:
#     if score > max:
#         max = score
# print(f"최대값은 {max}")



# # Q10. 100이하의 점수 5개를 입력 받아 최소값을 구하시오.

# # 1)
# min = 100

# for i in range(5):
#     score_1 = int(input("점수 입력: "))

#     if score_1 < min:
#         min = score_1
# print(f"최소값은 {min}")

# # 2)
# s1, s2, s3, s4, s5 = map(int,input("100이하 정수 입력: ").split())

# jum = (s1, s2, s3, s4, s5)
# min = 100

# for jum in jum:
#     if jum < min:
#         min = jum
# print(f"최소값은 {min}")



# # Q11. 5개의 점수를 입력 받아 최대값과 최소값을 제외한 나머지 점수의 합계와 평균을 구하시오.

# # 1)
# maxi = 0
# mini = 100
# total = 0

# for i in range(5):
#     jumsu = int(input("점수 입력: "))

#     total += jumsu

#     if jumsu > maxi:
#         maxi = jumsu
#     if jumsu < mini:
#         mini = jumsu

# total_1 = total - (maxi + mini)
# avg = total_1 / 3
# print(f"최대값, 최소값 제외한 점수의 합계는 {total_1}, 평균은 {avg}")

# # 2)
# sc1, sc2, sc3, sc4, sc5 = map(int,input("점수 입력: ").split())

# su = (sc1, sc3, sc4, sc4, sc5)
# max_1 = 0 
# min_1 = 100

# for su in su:
#     if su > max_1:
#         max_1 = su
#     if su < min_1:
#         min_1 = su

# total = sc1 + sc2 + sc3 + sc4 + sc5 - (max_1 + min_1)
# avg = total / 3
# print(f"최대,최소값을 제외한 점수의 합계는 {total}, 평균은 {avg}")