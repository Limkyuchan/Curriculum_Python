
# # 반복문

# # Q1. 30cm 자를 만들고 길이를 입력하면 그 위치를 화살표로 표시하는 프로그램을 작성 (ㅂ 한자키)

# # 1)
# st = "┌"
# for i in range(29):
#     st += "─"
# st += "┐"

# st_1 = ""
# for i in range(31):
#     st_1 += "│"

# user = int(input("길이 입력(cm) : "))
# print(st)
# print(st_1)

# for i in range(31):
#     if st_1[user] == st_1[i]:
#         print(" "*user + "↑")
#         break

# # 2)
# cm = int(input("cm 입력: "))

# for i in range(31):
#     if i == 0:
#         print("┌", end = "")
#     elif i == 30:
#         print("┐", end = "")
#     else: 
#         print("─", end = "")
# print()

# for i in range(31):
#     print("│", end = "")
# print()

# for i in range(31):
#     if i != cm:
#         print(" ", end = "")
#     if i == cm:
#         print("↑", end = "")
# print()



# # Q2. 현재 3분 50초 분량의 노래가 있다. 지금까지 진행된 노래 분량을 입력 받아 그림으로 표시하고
# #     몇% 진행됐는지 수치로 나타내는 프로그램을 작성하시오.

# sing = 230
# play = int(input("재생시간: "))

# per = int((play/sing)*100)

# for i in range(101):
#     if per == i:
#         print("■"* int(i/10), end = "")
# print(f" {per}%")



# # Q3. 다음과 같은 결과가 나올 수 있도록 프로그램을 작성하시오.

# for i in range(3):
#     for j in range(5):
#         print(i+3, end = " ")
#         i += 1
#     print()


# # Q4. 두 수를 입력 받아 큰 수에서부터 작은 수 까지 출력되도록 프로그램 작성.

# a = int(input("수를 입력하세요: "))
# b = int(input("수를 입력하세요: "))

# print("출력: ", end = " ")
# for i in range(a, b-1, -1):
#     print(i, end = " ")
# for i in range(b, a-1, -1):
#     print(i, end = " ")
# print()


# # Q5. 수를 입력 받아 0부터 입력 받은 수까지 3의 배수를 출력하도록 프로그램을 작성. (단, 0은 제외)

# su = int(input("수를 입력하세요: "))

# print("출력: ", end = " ")
# for i in range(1,su+1):
#     if i % 3 == 0:
#         print(i, end = " ")
# print()



# # Q6. 수를 입력 받아 0을 제외한 7의 배수를 입력 받은 수 만큼 출력하시오
# #   수를 입력하세요 4       출력: 7 14 21 28

# # 1)
# N = int(input("수 입력: "))

# print("출력: ", end = " ")
# for i in range(1, N * 7 + 1):
#     if i % 7 == 0:
#         print(i, end = " ")
# print()

# # 2)
# num = int(input('수 입력:'))
# for i in range(1,num+1):
#     print(i*7,end=" ")



# # Q7. 수를 입력 받아 1부터 입력 받은 수 사이의 2의 배수와 3의 배수를 출력. (단, 2와 3의 공배수는 제외)

# su = int(input("수를 입력하세요: "))

# print("2의 배수 : ", end = " ")
# for i in range(1, su+1):
#     if i % 2 == 0 and i % 3 == 0:
#         continue
#     elif i % 2 == 0:
#         print(i, end = " ") 
# print()
# print("3의 배수 : ", end = " ")
# for i in range(1, su+1):
#     if i % 2 == 0 and i % 3 == 0:
#         continue
#     elif i % 3 == 0:
#         print(i, end = " ") 
# print()



# # Q8. 다음과 같은 결과가 나올 수 있도록 프로그램을 작성하시오.

# for i in range(1,4):
#     for j in range(1,5):
#        print(i * j, end = " ")
#     print()



# # Q9. 다음과 같이 나올 수 있도록 프로그램을 작성하시오

# a = int(input("수를 입력하세요: "))
# a1 = a*2 + 1

# for i in range(a1):
#     if i % a == 0:
#         print("■"*5)
#     else:
#         print("□"*5)



# # Q10. 구구단을 다음과 같이 출력되도록 프로그램을 작성하시오.

# # 1) 세로 출력
# dan = int(input("단을 입력하세요: "))
# print(f"=== {dan}단 ===")
# print()
# for i in range(1,10):
#     print(f"{dan} x {i} = {dan*i}")
# print()

# # 2) 가로 출력
# dan2 = int(input("단을 입력하세요: "))
# print(f"=== {dan2}단 ===")
# print()
# for i in range(1,10):
#     print(f"{dan2} x {i} = {dan2*i}", end = "\t")
# print()



# # Q11. 구구단을 다음과 같이 출력되도록 프로그램을 작성하시오.

# number = int(input("단을 입력하세요: "))
# for i in range(1):
#     print(f"=== {number}단 ===")
#     print()
#     for j in range(1,10):
#             print(f"{number} x {j} = {number * j}", end = "\t")
#             if j == 5:
#                 print()
#     print()



# # Q12. 구구단을 다음과 같이 출력되도록 프로그램을 작성하시오.

# # 띄어쓰기로 공간
# for i in range(1, 10):
#     for j in range(2, 10):
#         if i * j < 10:
#             print(f"{j} x {i} =  {j*i}", end = "\t")
#         else:
#             print(f"{j} x {i} = {j*i}", end = "\t")
#     print()

# # 서식문자로 공간
# for i in range(1,10):
#     for j in range(2,10):
#         print("{} x {} = {:2d}".format(j, i, j*i), end = "  ")
#     print()

