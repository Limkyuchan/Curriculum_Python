class MyStr:
    def __init__(self, s=''):
        self.s = s
    def size(self):
        return len(self.s)

class MyStr2(MyStr):
    def __init__(self, s=''):
        super().__init__(s)
    
    def upper_count(self):
        result = 0
        for ch in self.s:
            if 'A' <= ch <= 'Z':
                result += 1
        return result

class MyStr3(MyStr2):
    def __init__(self, s=''):
        super().__init__(s)
    
    def lower_count(self):
        result = 0
        for ch in self.s:
            if 'a' <= ch <= 'z':
                result += 1
        return result

ms1 = MyStr('hello WelcomE!')
print(ms1.size())
print()


ms2 = MyStr2('hello WelcomE!')
print(ms2.size())
print(ms2.upper_count())
print()


ms3 = MyStr3('hello WelcomE!')
print(ms3.size())
print(ms3.upper_count())
print(ms3.lower_count())
print()