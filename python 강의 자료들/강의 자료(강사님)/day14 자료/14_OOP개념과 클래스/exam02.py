class Counter:
    def __init__(self, num = 0):
        self.setCount(num)
    def increment(self):
        self.cnt += 1
    def decrement(self):
        self.cnt -= 1
    def setCount(self, num): # setter
        self.cnt = num
    def getCount(self): # getter
        return self.cnt

cnt1 = Counter()
cnt2 = Counter(10)
cnt1.increment()
cnt1.increment()
cnt2.increment()
print(cnt1.getCount())
print(cnt2.getCount())

cnt1.cnt = 100
print(cnt1.cnt)


