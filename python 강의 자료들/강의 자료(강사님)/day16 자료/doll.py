class Battery:
    def __init__(self):
        self.charge = 100

    def use(self, amount):
        if self.charge - amount < 0:
            self.charge = 0
        else:
            self.charge -= amount

    def get_charge(self):
        return self.charge


class TalkingDoll:
    def __init__(self):
        self.__battery = None
        self.__message = '녹음된 메시지가 없습니다.'

    def insert_battery(self, battery):
        self.__battery = battery

    def remove_battery(self):
        battery = self.__battery
        self.__battery = None
        return battery

    def record_message(self, message):
        need = 14
        if not self.__battery:
            return
        if self.__battery.get_charge() > need:
            self.__message = message
            self.__battery.use(need)

    def talk(self):
        need = 10
        if not self.__battery:
            print("건전지 없음.")
            return
        if self.__battery.get_charge() > need:
            print(self.__message)
            self.__battery.use(need)
        else:
            print("건전지 용량 부족.")

# Battery기본 용량:100
doll = TalkingDoll()
doll.insert_battery(Battery())

doll.talk() # 10만큼 사용 -> 누적 10
doll.record_message('달링알러뷰') # 14만큼 사용 -> 누적 24
doll.talk() # 10 -> 누적 34
doll.talk() # 10 -> 누적 44
doll.talk() # 10 -> 누적 54
doll.record_message('알럽알럽') # 14 -> 누적 68
doll.talk() # 10 -> 누적 78
doll.record_message('뭐라고 녹음하지?') # 14 -> 누적 92
doll.talk() # 건전지 용량 부족 -> 남음 8
doll.talk() # 건전지 용량 부족 -> 남음 8

removed_battery = doll.remove_battery() # 배터리 제거
print('꺼낸 전지 용량:', removed_battery.get_charge())
doll.talk() # 건전지 없음

batt = Battery() # 새 배터리 생성
doll.insert_battery(batt) # 건전지 삽입
doll.talk() # 인형 동작

removed_battery = doll.remove_battery() # 배터리 제거
doll.talk() # 건전지 없음
print('꺼낸 전지 용량:', removed_battery.get_charge())

