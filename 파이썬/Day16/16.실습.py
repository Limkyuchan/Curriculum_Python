
# # OOP & Class

# # Q1. 말하는 인형과 건전지 구현

class Battery():

    def __init__(self):
        self.capacity = 100

    def useBattery(self, use):
        self.capacity -= use
        if self.capacity < 0 :
            self.capacity += use
            return False
        else:
            return True

    def getCharge(self):
        return self.capacity
    

class TalkingDoll:

    def __init__(self):
        self.message = "녹음된 메시지가 없습니다."
        self.battery = None

    def insert_battery(self, battery):
        self.battery = battery
        
    def remove_battery(self):
        emptybattery = self.battery
        self.battery = None
        return emptybattery

    def record_message(self, message):
        if not self.battery:
            return
        
        if self.battery.getCharge() >= 14:
            self.message = message
            self.battery.useBattery(14)
        
    
    def talk(self):
        if not self.battery:
            print("건전지 없음")
            return
        
        if self.message == None:
            print(self.message) 
        elif self.battery.getCharge() >= 10:
            print(self.message)
            self.battery.useBattery(10)
        else:
            print("건전지 용량 부족")


doll = TalkingDoll()
doll.insert_battery(Battery())

doll.talk()
doll.record_message("달링알러뷰")
doll.talk()
doll.talk()
doll.talk()
doll.record_message("알럽알럽")
doll.talk()
doll.record_message("뭐라고 녹음하지?")
doll.talk()
doll.talk()

removed_battery = doll.remove_battery()
print(f"꺼낸 전지 용량: {removed_battery.getCharge()}")
doll.talk()

batt = Battery()
doll.insert_battery(batt)
doll.talk()

removed_battery = doll.remove_battery()
print(f"꺼낸 전지 용량: {removed_battery.getCharge()}")
doll.talk()





# Q2. 5명의 이름과 나이를 저장하고 출력하는 프로그램 작성

class Person:

    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age
        self.li = []

    def saveInfo(self):
        self.cnt = int(input("몇 명 정보? "))
        for i in range(self.cnt):
            self.name = input("이름: ")
            self.age = int(input("나이: "))
            self.li.append([self.name, self.age])
        
    def printInfo(self):
        print()
        for i in range(self.cnt):
            print(f"{i+1}정보")
            print(f"이름: {self.li[i][0]}, 나이: {self.li[i][1]}세")


p1 = Person()
p1.saveInfo()
p1.printInfo()

