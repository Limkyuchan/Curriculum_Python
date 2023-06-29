
# 파이썬 Collection 자료형

# Q1 ~ Q3. 다음과 같은 튜플 생성
base_tup = (32, 12, 54, 22, 76, 77, 45, 44, 77, 54, 32)

# Q1. 생성한 튜플의 중복을 제거하여 unique_list 이름의 리스트에 저장
unique_list = set(base_tup)
unique_list = list(unique_list)
print(f"unique_list : {unique_list}")

# Q2. 알파벳을 키로 하여 unique_list 의 값들을 unique_dict 이름의 딕셔너리로 저장
unique_dict = {}
n = 65
for key in unique_list:
    unique_dict[chr(n)] = key
    n += 1
print(f"unique_dict : {unique_dict}")

# Q3. 딕셔너리에서 값을 기준으로 오름차순으로 정렬하여 sort_tup 이름의 튜플에 저장하고 출력
sort_tup = sorted(unique_dict.items(), key = lambda item: item[1] )
sort_tup = tuple(sort_tup)
print(f"sort_tup : {sort_tup}")


# Q4. 로또 1 ~ 100회 추첨 번호 통계 구하기
from random import randint

# 1)
print("="*10, "1 ~ 100회 당첨 번호", "="*10)
print()
total_li = []
for i in range(1,101):
    li = []
    while len(li) < 7:
        su = randint(1,45)
        if su < 10:
            su = str(su)
            su = "0" + su

        if su not in li:
            li.append(su)

    total_li += li

    if i < 10:
        i = str(i)
        i = "0" + i

    print(f"■{i}회차■  {li[0]} {li[1]} {li[2]} {li[3]} {li[4]} {li[5]}\tBonus[{li[-1]}]")

print()
total_li = list(map(int, total_li))

print("="*27, "1 ~ 100회 당첨 번호 통계", "="*27)
print()

for i in range(1,46):
    if i < 10:
        i = str(i)
        i = "0" + i

    result = total_li.count(int(i))
    if result < 10:
        result = str(result)
        result = "0" + result
    
    print(f"[{i}]번 : ({result})회", end = "\t")

    if int(i) % 5 == 0:
        print()
        
print()
print()


# 2) 딕셔너리 활용

# 로또 번호 랜덤 수 7개 추출
def random_number(n):
    number = set()
    while len(number) < 7:
        a = randint(1,45)
        number.add(a)
    return number

numbers = []
dict = {}
for i in range(1,101):
    dict[i] = random_number(i)
    numbers += random_number(i)

# dict = {}
# numbers = []

# for i in range(1,101):
#     number = set()
#     while len(number) < 7:
#         su = randint(1,45)
#         number.add(su)
#     dict[i] = number
#     numbers += number


# 임의 당첨 번호 생성
for i in range(1,101):
    print(f"■{i}회차■  " , end = " ")
    for j in range(7):
        if j == 6:
            print(f"\tBonus[{list(dict[i])[j]}]")
        else:
            print(f"{list(dict[i])[j]}", end = " ")

# 당첨 번호 통계 생성
for i in range(1,46):
    if i < 10:
        i = str(i)
        i = "0" + i
    print(f"[{i}]번: ({numbers.count(int(i))})회", end = "\t")
    
    if int(i) % 5 == 0:
        print()







