
# < 입력받는 방법 >
a, b, c = input("입력: ").split()
total = int(a) + int(b) + int(c)

a, b, c = map(int,input("입력: ").split())
total = a + b + c

print(total)


## < 객체와 참조의 이해! >
#   => ppt 수업자료 참고
# < 비교 연산자  is, is not >
a, b = "hello", "hello"

print(a,b)
print(id(a))
print(id(b))

print(a == b)
print(a is b)           # 객체를 비교   True

print(a is not b)       # 객체를 비교   False
print(a != b)

print()

c = "hello"
d = input("입력: ")

print(id(c))
print(id(d))

print(c == d)
print(c is d)           # 객체를 비교   False

print(c is not d)       # 객체를 비교   True
print(c != d)



# < 논리 연산자 >

# AND  논리곱  (2항     ㅁ and ㅁ)
# OR   논리합  (2항     ㅁ or  ㅁ)
# Not         (단항     not ㅁ  )

# short - circuit 평가 (논리연산에서만 의미가 있음.)
# and 연산 : 첫 번째 조건이 거짓이면 뒤의 조건을 보지 않는다. ex) False and ... (확인 안함)
#  or 연산 : 첫 번째 조건이 참이면 뒤의 조건을 보지 않는다.   ex) True or ... (확인 안함)

# Q1. 논리 연산자 이해
# 다음 예제의 실행 결과를 이해하시오.

print("0 and 1 = ", 0 and 1, bool(0 and 1))     # and : 0(False) and ...     -> 0 -> bool(0) : False
print("2 or 3 = ", 2 or 3, bool(2 or 3))        #  or : 2(True) or ..        -> 2 -> bool(2) : True 
print("2 and 4 = ", 2 and 4, bool(2 and 4))     # and : 2(True) and 4(True)  -> 4 -> bool(4) : True
print("0 or 3 = ", 0 or 3, bool(0 or 3))        #  or : 0(False) or 3(True)  -> 3 -> bool(3) : True
                                                # bool(값)에서 값이 0인 경우 False 그 외의 수는 True



# < 제어문 >

# 분기문 : 조건에 따른 흐름 분기
# 반복문 : 조건에 따라 코드 반복
