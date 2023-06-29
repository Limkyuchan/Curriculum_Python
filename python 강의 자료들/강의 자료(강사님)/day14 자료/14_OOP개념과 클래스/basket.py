class Counter:
    def __init__(self, count = 0, interval = 1):
        self.__count = count
        self.__interval = interval
    def increment(self):
        self.count += self.interval
    @property
    def count(self):
        return self.__count
    @property
    def interval(self):
        return self.__interval
    @count.setter
    def count(self, count):
        self.__count = count
    @interval.setter
    def interval(self, interval):
        self.__interval = interval
    def init(self):
        self.count = 0
        self.interval = 1
    def __str__(self):
        return f'count={self.__count},interval={self.__interval}'

# 카운트 객체 테스트
# cnt1 = Counter()
# cnt1.increment()
# cnt1.increment()
# print(cnt1.count)    
# cnt1.init()
# cnt1.increment()
# cnt1.increment()
# print(cnt1.count)    
# cnt1.count = 10
# print(cnt1.count)    
# cnt1.interval = 2
# cnt1.increment()
# print(cnt1.count)    

class BasketCounter:
    def __init__(self):
        self.__goal = [
            Counter(),
            Counter(),
            Counter(),
            Counter()
        ]
        self.__score = [
            Counter(),
            Counter(count=0, interval=2),
            Counter(count=0, interval=3),
            Counter()
        ]
    
    def goalin(self, goal):
        goal -= 1
        if 0 <= goal <= 3:
            self.__goal[goal].increment()
            self.__goal[3].increment()
            self.__score[goal].increment()
            self.__score[3].interval = goal+1
            self.__score[3].increment()

    @property
    def goal(self):
        return self.__goal

    @property
    def score(self):
        return self.__score


# 게임 시작
team1 = BasketCounter()

# 골인
team1.goalin(1)
team1.goalin(1)
team1.goalin(2)
team1.goalin(3)
team1.goalin(2)
team1.goalin(3)
team1.goalin(2)

goal = team1.goal
score = team1.score

# for g,s in zip(goal, score):
#     print(f'{s.interval}점슛 골:{g.count}개, 점수:{s.count}')

for i in range(3):
    print(f'{score[i].interval}점슛 골:{goal[i].count}개, 점수:{score[i].count}')
print(f'합계 골:{goal[3].count}개, 점수:{score[3].count}')