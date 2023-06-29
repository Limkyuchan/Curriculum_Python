
# 함수

# ## 함수 형태
# # 함수 형태 - 인자와 반환이 없는 함수
# def func1():
#     print('기능 동작')

# func1()
# print()

# # 함수 형태 - 인자는 있고 반환이 없는 함수
# def func2(n):
#     print(f'{n}으로 기능 동작')
# func2(1)
# print()

# # 함수 형태 - 인자는 없고 반환이 있는 함수
# def func3():
#     print('기능 동작')
#     return 10

# result = func3()
# print(result)
# print()

# # 함수 형태 - 인자와 반환이 있는 함수
# def func4(n1, n2):
#     return n1 + n2

# result = func4(10, 20)
# print(result)
# print()

# # 함수 형태 - 디폴트 매개변수
# def func5(n1=10, n2=20):
#     return n1 + n2

# print(func5())
# print(func5(100))
# print(func5(100, 200))
# print()

# # 일반 매개변수와 같이 활용
# #def func(name='noname', age): # 디폴트 값이 지정된 매개변수 다음에 일반 매개변수 선언 불가
# def func(age, name='noname'):
#     print(name)
#     print(age)

# func('Hong', 20)
# func(20)
# #func() 오류(age에 전달될 인자가 없으므로)

# # Packing/Unpacking
# fruits = ["apple", "banana", "cherry"]

# fruit1, fruit2, fruit3 = fruits
# print(fruit1)  
# print(fruit2)  
# print(fruit3)  

# numbers = [1, 2, 3, 4, 5]

# first, *middle, last = numbers 
# print(first)  
# print(middle) 
# print(last)   

# # 함수 형태 - 가변 인자(튜플)
# def sum(*args):
#     result = 0
#     for num in args:
#         result += num
#     return result

# print(sum(1,2,3))
# print(sum(1,2,3,4,5))
# values = [1,2,3,4,5]
# #print(sum(values)) # 오류
# print(sum(*values)) # Unpacking하여 전달

# print()

# #가변인자 일반인자 디폴트 매개변수 모두 적용
# def func(*args, n, s='de'):
#     print(f'n:{n}')
#     print(f's:{s}')
#     for ar in args:
#         print(ar)
#     print()

# func(1,2,3, n=10)
# func('hello', 'hi', n=20)
# a = ['a', 2, 'b', 3]
# func(a, 'A', n=30)
# #func(a) # n에 들어갈 인자가 없음 func() missing 1 required positional argument: 'n'



# # 함수 형태 - 키워드 인자
# def print_person_info1(name, age, city):
#     print("이름:", name)
#     print("나이:", age)
#     print("도시:", city)

# print_person_info1(age=20, city='서울', name='홍길동')
# print()

# # 함수 형태 - 가변 키워드 인자(딕셔너리)
# def print_person_info2(**kwargs):
#     print(kwargs)
#     print("이름:", kwargs['name'])
#     print("나이:", kwargs.get('age'))
#     print("도시:", kwargs['city'])

# print_person_info2(name='홍길동', age=20, city='서울')
# values = {'name':'홍길동', 'age':20, 'city':'서울'}
# #print_person_info2(k=values) # 오류 k=values와 같이 전달 필요
# print_person_info2(**values) # Unpacking하여 전달
# print()

# # 가변 키워드 인자를 받는 함수에서 packing/unpacking 사용
# def func(caller='Caller', **kargs):
#     keys = kargs.keys()
#     i = 0
#     for key in keys:
#         print(f'[{caller}]: {i}번째 인자{key}: {kargs[key]}')
#         i += 1
#     print()

# func(caller='홍', a=10)
# func(a=1, b=2, c=3)
# func(a='hello', b='hi')
# func(a=['1', '2', 3], b=(1, 2, 3), caller='박')
# values = {
#     'a':['1', '2', 3], 
#     'b':(1, 2, 3)
# }
# func(**values, caller='박')
# func(caller='최', **values)




# 가변 인자
# 1) 
# *가변 매개변수  => 자료 형태: 튜플
#    원형: def value(*args):          ==> packing (여러개의 값을 하나로 받음) 
#             print(args)                              
#
#         value("hello", "hi")      =>   ("hello", "hi")
#         value(1,2,3,4,5)          =>   (1,2,3,4,5)
#
#  만약 자료형이 리스트일 경우          ==> unpacking(*li) (여러개의 값을 가지고 있는 객체를 풀어줌)
#  li = [1,2,3,4,5]
#         value(li)       =>   ([1,2,3,4,5],)      
#  각각의 자료에 접근하기 위해서는 (*li)를 사용한다.  
#         value(*li)      =>   (1,2,3,4,5)          
#
# 2) 
# **가변 매개변수  => 자료 형태: 딕셔너리
#    원형: def value(**args):         ==> packing (여러개의 값을 하나로 받음)
#             print(args)                             
#
#        value(a=1, b=2, c=3)        =>  {"a" : 1, "b" : 2, "C" : 3}
#        value(a={1:1}, b={2:2})     =>  {"a" : {1:1}, "b" : {2:2}}
#
#  만약 자료형이 묶여있을 경우          ==> unpacking(*alp) (여러개의 값을 가지고 있는 객체를 풀어줌)
#  alp = {'a': 1, 'b': 2, 'c': 3}
#        value(va = alp)      =>  {"va" : {'a': 1, 'b': 2, 'c': 3}}   
#                                     key값과 value 값이 원하는 대로 매칭 안됨.
#        value(**alp)         =>  {'a': 1, 'b': 2, 'c': 3}


# 함수 인수에 초기값 지정
# 원형: def func(name = "noname", age = 0):
#           print(name)
#           print(age)
#      func()                =>   (noname, 0)
#      func("Lee", 20)       =>   ("Lee", 20)
#
# ※주의사항 : 왼쪽의 값에는 초기값이 지정 되어있지 않아도 괜찮으나,
#             오른쪽의 값에는 반드시 초기값이 지정 되어있어야 한다.
#             ex) def func(name, age = 0):           - O
#                 def func(name = "noname", age):    - X