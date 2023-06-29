# isinstance(참조, 타입) 객체(instance)의 클래스 타입을 확인
class 동물:
    def 먹는다(self):
        pass
    def 움직인다(self):
        pass
    def 호흡한다(self):
        pass
    def 소리낸다(self):
        pass

class 포유류(동물):
    def 호흡한다(self):
        print('폐 호흡')

class 어류(동물):
    def 호흡한다(self):
        print('아가미 호흡')

class 개(포유류):
    def 먹는다(self):
        print('개같이 먹는다.')
    def 움직인다(self):
        print('개같이 움직인다.')
    def 소리낸다(self):
        print('개같이 소리낸다.')
    def 개특징(self):
        print('개만 가지는 특징')

class 고양이(포유류):
    def 먹는다(self):
        print('고양이같이 먹는다.')
    def 움직인다(self):
        print('고양이같이 움직인다.')
    def 소리낸다(self):
        print('고양이같이 소리낸다.')
    def 고양이특징(self):
        print('고양이만 가지는 특징')

class 고래(포유류):
    def 먹는다(self):
        print('고래같이 먹는다.')
    def 움직인다(self):
        print('고래같이 움직인다.')
    def 소리낸다(self):
        print('고래같이 소리낸다.')
    def 고래특징(self):
        print('고래만 가지는 특징')

class 상어(어류):
    def 먹는다(self):
        print('상어같이 먹는다.')
    def 움직인다(self):
        print('상어같이 움직인다.')
    def 소리낸다(self):
        print('상어같이 소리낸다.')
    def 상어특징(self):
        print('상어만 가지는 특징')

animals = [고양이(), 개(), 고래(), 상어()]
for a in animals:
    print(type(a))
    a.먹는다()
    a.소리낸다()
    a.움직인다()
    a.호흡한다()
    if isinstance(a, 고양이): 
        a.고양이특징()
    elif isinstance(a, 개):
        a.개특징()
    elif isinstance(a, 고래):
        a.고래특징()
    elif isinstance(a, 상어):
        a.상어특징()
    print()