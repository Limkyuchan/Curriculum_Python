
# OOP & Class

# Q1. 상속 활용 개념이해 실습
# 1) 문자열을 저장하는 클래스 정의(MyStr)
#   - 길이를 반환하는 기능을 가짐

class MyStr:

    def __init__(self, st):
        self.st = st

    def size(self):
        return f"길이: {len(self.st)}"

# 2) 문자열을 저장하는 클래스 정의(MyStr2)
#   - 길이를 반환하는 기능을 가짐
#   - 대문자 개수를 반환하는 기능을 가짐

class MyStr2(MyStr):

    def __init__(self, st):
        super().__init__(st)

    def upper_count(self):
        cnt = 0
        for i in self.st:
            if 65 <= ord(i) <= 90:
                cnt += 1
        return f"대문자 개수: {cnt}"


# 3) 문자열을 저장하는 클래스 정의(MyStr3)
#   - 길이를 반환하는 기능을 가짐
#   - 대문자 개수를 반환하는 기능을 가짐
#   - 소문자 개수를 반환하는 기능을 가짐

class MyStr3(MyStr2):

    def __init__(self, st):
        super().__init__(st)
        
    def lower_count(self):
        cnt = 0
        for i in self.st:
            if 97 <= ord(i) <= 122:
                cnt +=1
        return f"소문자 개수: {cnt}"


ms1 = MyStr("hello WelcomE!")
print(ms1.size())
print()
ms2 = MyStr2("hello WelcomE!")
print(ms2.size())
print(ms2.upper_count())
print()
ms3 = MyStr3("hello WelcomE!")
print(ms3.size())
print(ms3.upper_count())
print(ms3.lower_count())







