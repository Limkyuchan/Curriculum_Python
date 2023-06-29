class 동물:
    def 움직인다(self):
        raise NotImplementedError('움직인다() 미구현')

class 고양이(동물):
    def 소리낸다(self):
        return '냐옹'
    def 움직인다(self): # 오버라이딩
        return '어슬렁어슬렁'

cat = 고양이()
print(cat.소리낸다())
print(cat.움직인다())