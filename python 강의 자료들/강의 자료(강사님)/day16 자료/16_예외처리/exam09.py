class 동물:
    def 움직인다(self):
        raise NotImplementedError('움직인다() 미구현')

class 고양이(동물):
    def 소리낸다(self):
        return '냐옹'

cat = 고양이()
print(cat.소리낸다())
print(cat.움직인다()) #NotImplementedError: 움직인다() 미구현 예외 발생