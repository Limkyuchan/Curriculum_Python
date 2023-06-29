
# 재귀함수 (강의자료 examq 14 ~ 15.py)

# Q1. 인자로 N을 전달하면 N에 대한 팩토리얼을 반환하는 함수(재귀)

def 팩토(N):
    if N == 1:
        return 1
    else:
        return N * 팩토(N-1)

N = int(input("수 입력: "))
print(팩토(N))


# Q2. 인자로 N을 전달하면 거꾸로 만든 수를 반환하는 함수(재귀)

def 거꾸로(st):
    if st == "":
        return st
    else:
        return 거꾸로(st[1:]) + st[0]

st = input("입력: ")
print(거꾸로(st))





# lambda함수

# Q1. 물체의 위치와 시간을 받아서, 등속 운동하는 물체의 속도를 계산하는 함수를 구현

calcu_velocity = lambda distance, time: round(distance / time, 2)

print(calcu_velocity(10000, 2))
print(calcu_velocity(13000, 1.7))


# Q2. 정수를 받아서, 해당 정수가 짝수인지 홀수인지 판별하는 함수를 구현

is_even = lambda number: number % 2 == 0

print(is_even(10))
print(is_even(9))


# Q3. 두 개의 정수를 받아서, 두 정수 중에서 큰 값을 반환하는 함수를 구현

find_max = lambda num1, num2: max(num1 , num2)

print(find_max(2,10))
print(find_max(10,2))


# Q4. 두 개의 문자열을 받아서, 두 문자열이 같은 지 비교하는 함수를 구현

compare_strings = lambda str1, str2: str1 == str2

print(compare_strings("Hello", "hello"))
print(compare_strings("Hello", "Hello"))


# Q5. 리스트를 받아서 리스트에 있는 모든 숫자의 합을 구하는 함수를 구현

calculate_sum = lambda numbers: sum(numbers)

print(calculate_sum([1,3,5,7,9]))
print(calculate_sum([2,4,6,8,10]))


# Q6. 다음 코드를 설명하세요.

def filter_strings(func, lst):
    for s in lst:
        if func(s):
            print(s)

lst = ["apple", "banana", "orange", "kiwi", "grape"]
check_length = lambda s: len(s) >= 5
filter_strings(check_length, lst)

"""
filter_strings 함수 호출
for문에서 s변수가 lst의 각각의 자료에 접근 
if문을 통해 s의 값을 check_length 함수로 확인
문자열의 길이가 5 이상 일 때 출력
"apple", "banana", "orange", "grape" 출력됨
"""


# Q7. 다음 코드를 설명하세요.

def find_number(func):
    for i in range(1, 11):
        if func(i):
            return i
        
greater_than_six = lambda x: x > 6
result = find_number(greater_than_six)
print(result)

"""
find_number 호출
for문에서 i가 1부터 10까지 반복
if문을 통해 i의 값을 greater_then_six 함수로 확인
i의 값이 6보다 큰지 확인
i의 값이 6보다 큰 7일때 7의 값을 return 하며 함수 종료
7 출력됨
"""



