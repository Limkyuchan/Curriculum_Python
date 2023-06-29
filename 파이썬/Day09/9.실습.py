from random import randint

# 리스트

# Q1 ~ Q4) 10, 17, 3, 9, 27, 10, 8, 9, 13, 21 값을 base_list 에 저장하고 시작  
base_list = [10, 17, 3, 9, 27, 10, 8, 9, 13, 21]
print(base_list)

# Q1. 위의 숫자(base_list)를 invert_list라는 배열에 거꾸로 입력하시오.

invert_list = list(reversed(base_list))
print(f"invert_list: {invert_list}")


# Q2. 위의 숫자(base_list)의 짝수번째 내용의 합과 홀수번째 내용의 합을 구하시오.

zak_hap = 0
hol_hap = 0
for i in range(len(base_list)):
    if i % 2 == 0:
        zak_hap += base_list[i]
    else:
        hol_hap += base_list[i]

print(f"짝수번째 합은 {zak_hap} 홀수번째 합은 {hol_hap}")


# Q3. 위의 숫자(base_list)를 sort_list 라는 배열에 내림차순으로 정렬하여 입력하시오.

sort_list = sorted(base_list, reverse = True)
print(f"sort_list: {sort_list}")


# Q4. 위의 숫자(base_list)를 높은 숫자가 1등이 되게 하여 rank_list 라는 배열에 순위를 입력하시오.

rank_list = []
for i in range(len(sort_list)):
    rank_list.append(f"{i+1}등 {sort_list[i]}")
print(f"rank_list: {rank_list}")


# Q5. 로또 예상 번호 생성하기 (중복 없이)

# 1)
lottonum = []
for i in range(6):
    num = randint(1,45)

    while num in lottonum:
        num = randint(1,45)

    lottonum.append(num) 
    
print(f"로또 번호: {sorted(lottonum)}")

# 2)
lottonum = []
while len(lottonum) < 6:
    num = randint(1,45)

    if num not in lottonum:
        lottonum.append(num)

print(f"로또 번호: {lottonum}")

# 3) flag 기법
lottonum = []
flag_list = list(range(45))

for i in range(45):
    flag_list[i] = False

while len(lottonum) < 6:
    num = randint(1,45)
    if flag_list[num-1] == False:
        lottonum.append(num)
        flag_list[num-1] = True
    else:
        continue

print(f"로또 번호: {lottonum}")

# 4) shuffle
lottonum = list(range(45))
for i in range(1,46):
    lottonum[i-1] = i

for i in range(10000):
    num1 = randint(1,45)
    num2 = randint(1,45)
    lottonum[num1-1],lottonum[num2-1] = lottonum[num2-1],lottonum[num1-1]

print(f"로또 번호: {lottonum[:6]}")