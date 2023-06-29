
# # while 반복문

# # Q1. 10이하의 정수를 입력하시오. (10이상이면 다시 입력 받도록)

# while True:
#     N = int(input("정수 입력(10 이하): "))

#     if N <= 10:
#         print(N)
#         break


# # Q2. 3의 배수를 판별하는 프로그램을 작성. (단, Q가 입력되면 종료)
# #    입력 받자 마자 제일 먼저 q인지 판별, 아니면 정수로 변환해서 3의 배수를 판별

# while True:
#     num = input("입력(종료시 Q): ")

#     if num == "Q":
#         print("프로그램이 종료됩니다.")
#         break
#     else:
#         if num.isnumeric():
#             num = int(num)
#             if num % 3 == 0:
#                 print(f"{num}은 3의 배수 입니다.")
#             else:
#                 print(f"{num}은 3의 배수가 아닙니다.")
#         else:
#             print("수를 입력하세요.") 


# # Q3. 1자리 숫자를 계속 입력 받아 합과 입력된 개수를 구하시오.
# #     (단, 2자리 이상의 숫자가 들어오면 입력된 2자리 이상의 수까지 계산하고 종료)

# cnt = 0
# hap = 0
# while True:
#     su = int(input("숫자 입력(한자리): "))

#     hap += su
#     cnt += 1

#     if su >= 10:
#         print("두 자리 이상 입력으로 프로그램 종료!")
#         break

# print(f"입력 받은 수의 합은 {hap}, 개수는 {cnt}개 입니다.")


# # Q4. 수를 입력 받아 거꾸로 수를 출력하도록 프로그램을 작성.
# #   입력: 123       출력: 321

# # 1) 인덱싱
# sut = input("수 입력: ")

# i = len(sut)
# while i > 0:
#     print(sut[i-1], end = "")
#     i -= 1
# print()

# # 2) 일의자리
# num = int(input("수 입력:"))    

# while num != 0:
#     result = num % 10
#     num = num // 10
#     print(result, end = "")
# print()

# # 3) 결과 x 10 하고 더해줌
# num = int(input("수 입력: "))
# result = 0
# while True:
#     result += num % 10
#     num = num // 10

#     if num == 0:
#         break
    
#     result *= 10
# print(result)


# # Q5. 쌀 100통이 저장되어 있고 쥐가 암수 1쌍이 있다. 쥐 한마리가 20g씩의 쌀을 먹고
# #     10일 마다 쥐의 수가 2배씩 증가한다. 며칠 만에 창고의 쌀이 모두 쥐의 먹이가 될까?
# #     그리고 쥐는 총 몇 마리 인가?  (쌀 한통은 80kg)

# ssal = 8000000
# day = 1
# g = 2

# while True:

#     if day % 10 == 0:
#         g *= 2

#     ssal -= g*20

#     if ssal <= 0:
#         print(f"{day}일, 쥐는 {g}마리")
#         break
    
#     day += 1


# # Q6. 체스 판의 첫번째 사각형에는 밀알 1개를, 두번째 사각형에는 밀알 2개를,
# #     세번째 사각형에는 밀알 4개... 등으로 총 64칸에 밀알을 2배씩 채워주기를 요구했다. 요구한 밀알 개수는?

# n = 1
# mil = 1
# total = 1
# while n < 64:
#     n += 1
#     mil *= 2 
#     total += mil

# print(f"요구한 밀알의 개수는 {total}개")


# # Q7. 사용자로부터 화폐금액을 입력 받아 화폐종류의 각 개수를 출력하세요. (변수만 사용)

# money = int(input("현재 금액 입력: "))

# m_50000 = money // 50000
# m_10000 = (money % 50000) // 10000
# m_5000 = (money % 10000) // 5000
# m_1000 = (money % 5000) // 1000
# m_500 = (money % 1000) // 500
# m_100 = (money % 500) // 100
# m_50 = (money % 100) // 50
# m_10 = (money % 50) // 10

# print(f"5만원 x {m_50000}, 1만원 x {m_10000}, 5천원 x {m_5000}, 1천원 x {m_1000}, \
# 500원 x {m_500}, 100원 x {m_100}, 50원 x {m_50}, 10원 x {m_10}")


# # Q8. 십진수를 이진수로 변환하는 프로그램을 작성하세요.( 10 => 1010 )

# num = int(input('수를 입력하세요. : '))

# st = ""
# while num != 0:
#     result = num % 2
#     st = str(result) + st
#     num = num // 2

# print(f"출력: {st}")


# # Q9. 정수를 입력받아 팩토리얼 계산하는 프로그램 작성.

# su = int(input("수 입력: "))
# result = 1

# while su > 0:
#     result *= su
#     su -= 1
# print(result)


# # Q10. 수를 입력 받아 1부터 입력 받은 값 까지의 합 구하고 (1)
# #      수를 입력 받아 1부터 입력 받은 값 까지의 합 구하고 (2)
# #      (1)과 (2)의 합(3)을 구하고, 1부터 (3)까지의 합을 구하시오.

# num = int(input("수 입력: "))
# hap1 = 0
# for i in range(1, num+1):
#     hap1 += i

# num2 = int(input("수 입력: "))
# hap2 = 0
# for i in range(1, num2+1):
#     hap2 += i

# hap = hap1 + hap2

# hap3 = 0
# for i in range(1, hap+1):
#     hap3 += i

# print(f"결과1: {hap1}")
# print(f"결과2: {hap2}")
# print(f"결과3: {hap3}")