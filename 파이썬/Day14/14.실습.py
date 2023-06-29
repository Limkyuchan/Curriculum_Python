
# OPP & Class

# # Q1. TV클래스를 정의하시오. (전원을 숫자 홀,짝으로 구분)   =>  Q1.1 방식으로!!

# class TV:

#     def __init__(self, brand, power = None, ch = None, vol = None):     # 생성자

#         self.brand = brand
#         self.ch = 0
#         self.vol = 0
#         self.power = 0

#         if power == None:               # 생성자 오버 로딩
#             self.power = 0
#         elif int(power) % 2 == 0:
#             self.power = 0
#         elif int(power) % 2 == 1:
#             self.power = 1

#         if ch == None:              
#             self.ch = 0
#         elif type(ch) == int:
#             self.ch = ch
#         else:
#             self.ch = 0

#         if vol == None:
#             self.vol = 0
#         elif type(vol) == int:
#             self.vol = vol
#         else:
#             self.vol = 0

#     def powerOnOff(self):
#         self.power += 1

#     def chUp(self):
#         self.ch += 1

#     def volUP(self):
#         self.vol += 1

#     def display(self):
#         print("="*15)
#         print(f"{self.brand} TV")

#         if self.power % 2 == 0:
#             print("전원 꺼짐")
#             print("="*15)
#             print()
#         else:
#             print("~"*8)
#             print(f"ch: {self.ch}")
#             print(f"vol: {self.vol}")
#             print("방송 중")
#             print("~"*8)
#             print("="*15)
#             print()

# tv1 = TV("삼성")
# tv2 = TV("엘지", 11, 15, 10)

# tv1.display()
# tv2.display()

# tv1.powerOnOff()
# tv1.display()
# tv2.display()

# tv1.chUp()
# tv1.volUP()
# tv1.display()



# # Q1-1. TV클래스를 정의하시오. (전원을 False,True 로 반전시키며 구분)

# class TV:

#     def __init__(self, brand, power = None, ch = None, vol = None):     # 생성자

#         self.brand = brand
#         self.ch = 0
#         self.vol = 0
#         self.power = False

#         if power == None:
#             self.power = False
#         elif power == "on":
#             self.power = True
#         elif power == "off":
#             self.power = False

#         if ch == None:              
#             self.ch = 0
#         elif type(ch) == int:
#             self.ch = ch
#         else:
#             self.ch = 0

#         if vol == None:
#             self.vol = 0
#         elif type(vol) == int:
#             self.vol = vol
#         else:
#             self.vol = 0


#     def powerOnOff(self):
#         if self.power == False:
#             self.power = True
#         else:
#             self.power = False
#         self.display()              # 전원 끄고 킨 결과 바로 출력하여 확인

#     def chUp(self):
#         self.ch += 1
#         self.display()              # 채널 올린 결과 바로 출력하여 확인

#     def volUP(self):
#         self.vol += 1
#         self.display()              # 볼륨 올린 결과 바로 출력하여 확인

#     def display(self):
#         print("="*15)
#         print(f"{self.brand} TV")

#         if self.power == True:
#             print("~"*8)
#             print(f"ch: {self.ch}")
#             print(f"vol: {self.vol}")
#             print("방송 중")
#             print("~"*8)
#         elif self.power == False:
#             print("전원 꺼짐")

#         print("="*15)
#         print()


# tv1 = TV("삼성")
# tv2 = TV("엘지", "on", 15, 10)

# tv1.display()
# tv2.display()

# tv1.powerOnOff()
# tv1.display()
# tv2.display()

# tv1.chUp()
# tv1.volUP()





# # Q2. 앞서 만든 TV 클래스를 사용하는 리모컨을 직접 정의해보기
# # 리모컨의 기능과 속성을 생각하여 분류
# # ex) 속성: TV를 참조해야 한다는 것을 이해
# #     기능: 전원, 채널변경, 볼륨변경 등
# # 리모컨의 속성(값)은 변수로, 기능은 멤버 메소드로 정의
# # 작성 후 객체를 생성하여 기능 테스트.  리모컨이 TV를 사용한다는 것을 표현하는 것

# class TV:

#     def __init__(self, brand, ch = None, vol = None, power = None):

#         self.brand = brand
#         self.ch = 0
#         self.vol = 0
#         self.power = False

#         if power == None:                
#             self.power = False
#         elif power == "on":
#             self.power = True
#         elif power == "off":
#             self.power = False

#         if ch == None:              
#             self.ch = 0
#         elif type(ch) == int:
#             self.ch = ch
#         else:
#             self.ch = 0

#         if vol == None:
#             self.vol = 0
#         elif type(vol) == int:
#             self.vol = vol
#         else:
#             self.vol = 0

#     def powerOnOff(self):
#         if self.power == False:
#             self.power = True
#         else:
#             self.power = False
#         self.display()             

#     def chUp(self):
#         self.ch += 1
#         self.display()            

#     def volUp(self):
#         self.vol += 1
#         self.display()              

#     def display(self):
#         print("="*15)
#         print(f"{self.brand} TV")

#         if self.power == True:
#             print("~"*8)
#             print(f"ch: {self.ch}")
#             print(f"vol: {self.vol}")
#             print("방송 중")
#             print("~"*8)
#         elif self.power == False:
#             print("전원 꺼짐")
#         print("="*15)
#         print()

# class Remocon:

#     def __init__ (self, tv):
#         self.tv = tv

#     def remoconPower(self):
#         self.tv.powerOnOff()

#     def remoconChUp(self):
#         self.tv.chUp()
 
#     def remoconVolUp(self):
#         self.tv.volUp()

#     def remoconDisplay(self):
#         self.tv.display()


# tv1 = TV("삼성")
# tv2 = TV("엘지")

# remocon1 = Remocon(tv1)
# remocon2 = Remocon(tv2)

# remocon1.remoconDisplay()
# remocon2.remoconDisplay()

# remocon1.remoconPower()
# remocon1.remoconChUp()
# remocon1.remoconVolUp()
# remocon1.remoconPower()

# remocon2.remoconPower()
# remocon2.remoconChUp()
# remocon2.remoconChUp()
# remocon2.remoconVolUp()