
# # file Input/Output

# from random import randint

## 로또 번호 문제
# # Q1. 로또 당첨 번호를 임의로 100회차 만큼 생성하여 "로또.txt" 파일에 저장
# file_lotto = open("파이썬/Day13/로또.txt", "w", encoding = "utf-8")
# file_lotto.write("\t  < 1회 ~ 100회차 로또 당첨 번호 >\n\n")
# lotto_numbers = []    
# for i in range(1,101):
#     number = []
#     while len(number) < 7:
#         su = randint(1,45)
#         if su not in number:
#             number.append(su)
#     lotto_numbers += number
#     file_lotto.write(f"{i}회차 로또번호: {number}\n")
# file_lotto.close()
# print()

# # Q1. 로또 저장 방식
# # file_lotte = open("파이썬/Day13/로또.txt", "w", encoding = "utf-8")

# # num = {}
# # for i in range(1,101):
# #     number = []
# #     while len(number) < 7:
# #         su = randint(1,45)
# #         if su not in number:
# #             number.append(su)
# #     num[i] = number

# # for i in num.items():
# #     tmp = str(i).replace("[", "").replace(" ", "").replace("]", "|").replace("(","").replace(")","")
# #     file_lotte.write(tmp)

# # file_lotte.close()


# # Q2. "로또.txt"파일을 읽어 들여 각 번호의 빈도를 구하여 "빈도.txt" 파일에 저장
# file_lotto = open("파이썬/Day13/로또.txt", "r", encoding= "utf-8")
# fre = []
# for i in range(1,46):
#     fre.append([i, lotto_numbers.count(i)])

# file_fre = open("파이썬/Day13/빈도.txt", "w", encoding = "utf-8")
# file_fre.write("각 번호의 빈도수\n\n")
# for i in range(1,46):
#     file_fre.write(f"{i}번 : {fre[i-1][1]}회\n")

# file_lotto.close()
# file_fre.close()
# print()

# # Q3. "빈도.txt" 파일을 읽어 들여 콘솔에 내림차순으로 출력한다.
# file_fre = open("파이썬/Day13/빈도.txt", "r")
# most_fre = sorted(fre, key = lambda x:x[1], reverse = True)
# print("================== 각 번호의 빈도수 (로또 번호, 나온 횟수) ==================")
# print()
# for i in range(1,46):
#     if i < 10:
#         i = str(i)
#         i = "0" + i
#     print(f"{i}등: {most_fre[int(i)-1]}", end = "\t")
#     if int(i) % 5 == 0:
#         print()
# print()
# print("="*77)

# # Q4. 출력된 내용에서 빈도가 가장 낮은 수 6개를 오늘 구매한다.
# print()
# print("오늘 구매할 숫자 6개는 : ", end = " ")
# su = 39
# for i in range(6):
#     print(most_fre[su][0], end = " ")
#     su += 1
# print("입니다. (Good Luck!)")
# print()
# file_fre.close()








## 위의 Q1 ~ Q4. 로또 문제 CSV 파일 추가
from random import randint

# Q1. 로또 당첨 번호를 임의로 100회차 만큼 생성하여 "로또.txt" 파일에 저장
file_lotto = open("파이썬/Day13/로또.txt", "w", encoding = "utf-8")
file_lotto.write("\n")
lotto_numbers = []    
for i in range(1,101):
    number = []
    while len(number) < 7:
        su = randint(1,45)
        if su not in number:
            number.append(su)
    lotto_numbers += number
    number = str(number).replace("[","").replace("]","")
    file_lotto.write(f"{i}, {number}\n")
file_lotto.close()
print()

# Q2. "로또.txt"파일을 읽어 들여 각 번호의 빈도를 구하여 "빈도.txt" 파일에 저장
file_lotto = open("파이썬/Day13/로또.txt", "r", encoding= "utf-8")
freq = []
for i in range(1,46):
    freq.append([i, lotto_numbers.count(i)])

file_freq = open("파이썬/Day13/빈도.txt", "w", encoding = "utf-8")
file_freq.write("\n")
for i in range(1,46):
    file_freq.write(f"{freq[i-1][0]}, {freq[i-1][1]}\n")

file_lotto.close()
file_freq.close()
print()

# Q3. "빈도.txt" 파일을 읽어 들여 콘솔에 내림차순으로 출력한다.
file_freq = open("파이썬/Day13/빈도.txt", "r")
most_freq = sorted(freq, key = lambda x:x[1], reverse = True)
print("================== 각 번호의 빈도수 (로또 번호, 나온 횟수) ==================")
print()
for i in range(1,46):
    if i < 10:
        i = str(i)
        i = "0" + i
    print(f"{i}등: {most_freq[int(i)-1]}", end = "\t")
    if int(i) % 5 == 0:
        print()
print()
print("="*77)

# Q4. 출력된 내용에서 빈도가 가장 낮은 수 6개를 오늘 구매한다.
print()
print("오늘 구매할 숫자 6개는 : ", end = " ")
su = 39
for i in range(6):
    print(most_freq[su][0], end = " ")
    su += 1
print("입니다. (Good Luck!)")
print()
file_freq.close()

# 로또 결과 파일 CSV형식으로 저장.
file_lottecsv = open("파이썬/Day13/로또.csv", "w")
file_lottecsv.write(f"No, Number1, Number2, Number3, Number4, Number5, Number6, Bonus")

file_lotto = open("파이썬/Day13/로또.txt", "r")
for i in range(101):
    file_lottecsv.write(file_lotto.readline())

file_lottecsv.close()
file_lotto.close()

# 빈도 결과 파일 CSV형식으로 저장.
file_freqcsv = open("파이썬/Day13/빈도.csv", "w")
file_freqcsv.write(f"Number, Frequency")

file_freq = open("파이썬/Day13/빈도.txt", "r")
for i in range(47):
    file_freqcsv.write(file_freq.readline())

file_freqcsv.close()
file_freq.close()
