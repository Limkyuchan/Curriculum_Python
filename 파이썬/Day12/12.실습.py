
# Comprehension (day12자료(강사님) quiz 파일)

# Q1. 리스트 컴프리헨션을 사용하여 1 ~ 100 사이의 홀수 숫자 리스트 생성
odd_numbers = [num for num in range(1, 101) if num % 2 == 1]
print(odd_numbers)

# Q2. 집합(set) 컴프리헨션을 사용하여 1 ~ 10까지의 제곱수 집합(set) 생성
squares = {num**2 for num in range(1,11)}
print(squares)

# Q3. 딕셔너리 컴프리헨션을 사용하여 15 ~ 25 사이의 숫자와 제곱수 쌍의 딕셔너리 생성
number_square_pairs = {num: num ** 2 for num in range(15, 26)}
print(number_square_pairs)

# Q4. 리스트 [1, 2, 3, 2, 4, 2, 5]에서 index()함수를 활용하여 값 2의 모든 인덱스를 리스트로 생성
li = [1, 2, 3, 2, 4, 2, 5]
indices = [num for num in range(len(li)) if li[num] == 2]
print(indices)












# File Input/Output

# Q1. 다음과 같이 동작하도록 작성하세요.
file_name = input(f"저장할 파일명: ")
name = input("이름: ")
age = int(input("나이: "))
file = open(f"{file_name}", "w", encoding = "utf-8")
file.write(f"이름: {name}\n나이: {age}")
file.close()
print("저장되었습니다.")
print()

# Q1-1. 
file_name2 = input("불러올 파일명: ")
f = open(f"{file_name2}", "r", encoding = "utf-8")
print(f.read())
f.close()
print("모두 읽었습니다.")
print()











# Q2. "샘플문서.txt" 파일을 이용하여 다음 정보를 파악하시오.

# 1) 전체 글자 개수(공백 제외)
f = open("파이썬/Day12/샘플문서.txt", "r")
st = f.read()

total_str = len(st.replace(" ",""))
print(f"전체 글자 개수(공백 제외): {total_str}")
f.close()
print()


# 2) 각 알파벳 개수(대소문자 구분X)
f = open("파이썬/Day12/샘플문서.txt", "r")
st = f.read()

count_alpa = []
su = 65
su2 = 97
print("각 알파벳 개수")
for i in range(26):
    print(f"{chr(su2)} : {st.count(chr(su)) + st.count(chr(su2))}개")
    count_alpa.append([chr(su2), st.count(chr(su)) + st.count(chr(su2))])
    su += 1
    su2 += 1

most_alpa = sorted(count_alpa, key = lambda x: x[1], reverse = True)  
f.close()
print()


# 3) 단어의 개수
f = open("파이썬/Day12/샘플문서.txt", "r")
st = f.read()

words = st.split()
cnt_word = len(words)
print(f"단어의 개수: {cnt_word}")

li2 = []
for i in set(words):
    li2.append([i, words.count(i)])

most_words = sorted(li2, key = lambda x: x[1], reverse = True)
f.close()
print()


# 4) 각 특수문자 개수(공백 제외)
f = open("파이썬/Day12/샘플문서.txt", "r")
st = f.read()

li = []
for i in st.replace(" ",""):
    if 65 <= ord(i) <= 90:
        continue
    elif 97 <= ord(i) <= 122:
        continue
    elif i.isnumeric():
        continue
    else:
        li.append(i)

use = []
for i in set(li):
    use.append([i, li.count(i)])

print(f"각 특수문자 개수: {use}")
most_special = sorted(use, key = lambda x: x[1], reverse = True)
f.close()
print()

# 다음 내용을 "결과.txt" 파일에 출력
f = open("파이썬/Day12/결과.txt", "w", encoding = "utf-8")

f.write(f"가장 많이 사용된 알파벳은? {most_alpa[0][0]}\n")
f.write(f"가장 많이 사용된 단어는? {most_words[0][0]}\n")
f.write(f"가장 많이 사용된 특수문자는? {most_special[0][0]}\n")
f.close()











# Q2-2. 함수 사용
# 1) 전체 글자 개수(공백 제외)
f = open("파이썬/Day12/샘플문서.txt", "r")
st = f.read()

total_str = len(st.replace(" ",""))
print(f"전체 글자 개수(공백 제외): {total_str}")
f.close()
print()


# 2) 각 알파벳 개수(대소문자 구분X)
f = open("파이썬/Day12/샘플문서.txt", "r")
st = f.read()

print("각 알파벳 개수")

def cnt_alpa(n):
    count_alpa = []
    su = 65 + n
    su2 = 97 + n
    print(f"{chr(su2)} : {st.count(chr(su)) + st.count(chr(su2))}개")
    count_alpa.append([chr(su2), st.count(chr(su)) + st.count(chr(su2))])
    return count_alpa

total_alpa = []

for i in range(26):
    total_alpa += cnt_alpa(i)

most_alpa = sorted(total_alpa, key = lambda x: x[1], reverse = True)  
f.close()
print()


# 3) 단어의 개수
f = open("파이썬/Day12/샘플문서.txt", "r")
st = f.read()

words = st.split()
cnt_word = len(words)
print(f"단어의 개수: {cnt_word}")

li2 = []
for i in set(words):
    li2.append([i, words.count(i)])

most_words = sorted(li2, key = lambda x: x[1], reverse = True)
f.close()
print()


# # 4) 각 특수문자 개수(공백 제외)
f = open("파이썬/Day12/샘플문서.txt", "r")
st = f.read()

def choice_special(n):
    li2 = []
    if 65 <= ord(n) <= 90:
        pass
    elif 97 <= ord(n) <= 122:
        pass
    elif n.isnumeric():
        pass
    else:
        li2.append(n)
    return li2

use_spe = []
for i in st.replace(" ",""):
    use_spe += choice_special(i)

uses = []
for i in set(use_spe):
    uses.append([i, use_spe.count(i)]) 
print(f"각 특수문자 사용 개수: {uses}")

most_special = sorted(uses, key = lambda x: x[1], reverse=True)
f.close()
print()

# 다음 내용을 "결과.txt" 파일에 출력
f = open("파이썬/Day12/결과.txt", "w", encoding= "utf-8")

f.write(f"가장 많이 사용된 알파벳은? {most_alpa[0][0]}\n")
f.write(f"가장 많이 사용된 단어는? {most_words[0][0]}\n")
f.write(f"가장 많이 사용된 특수문자는? {most_special[0][0]}\n")
f.close()
