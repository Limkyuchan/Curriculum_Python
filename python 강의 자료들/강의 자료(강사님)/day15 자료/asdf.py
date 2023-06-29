#농구 점수 계산기 만들기(클래스를 이용)
#캡슐화, 은닉화, 생성자, self 이용하기
#생성자를 이용해서 count값 초기화하기(0 또는 임의 값으로 초기화)
#Getter, Seteer 사용하여 사용자 임의로 초기화가 가능하도록 작성
#<기능> 1,2,3점 메뉴 입력 시 해당 골 과 득점 입력
#각각 골의 수와 총 골의 수 개별 누적
#프로그램 종료 시(경기종료) 총점과 총 골 수 출력
#출력 모양은 자유!

class BasketballScoreCalculator:
    def __init__(self, count=0):
        self._count = count
        self._score = 0
        self._one_point_goals = 0
        self._two_point_goals = 0
        self._three_point_goals = 0
    
    def add_goal(self, goal, points):
        if goal == 1:
            self._one_point_goals = points
        elif goal == 2:
            self._two_point_goals = points
        elif goal == 3:
            self._three_point_goals = points
        else:
            print("1~3점 슛까지만 넣을수있습니다!")
            return
        
        self._score += points
        self._count += 1
    
    def get_total_score(self):
        return self._score
    
    def get_total_goals(self):
        return (self._one_point_goals + (self._two_point_goals * 2) + (self._three_point_goals * 3))
    
    def set_count(self, count):
        self._count = count
    
    def get_count(self):
        return self._count
    
    def set_score(self, score):
        self._score = score
    
    def get_score(self):
        return self._score
    
    def set_one_point_goals(self, goals):
        self._one_point_goals = goals
    
    def get_one_point_goals(self):
        return self._one_point_goals
    
    def set_two_point_goals(self, goals):
        self._two_point_goals = goals
    
    def get_two_point_goals(self):
        return self._two_point_goals
    
    def set_three_point_goals(self, goals):
        self._three_point_goals = goals
    
    def get_three_point_goals(self):
        return self._three_point_goals

if __name__ == '__main__':
    calc = BasketballScoreCalculator()
    
    while True:
        print("┌─────┐─────┐─────┐")
        print("│     │  골 │ 점수│")
        print("└─────┘─────┘─────┘")
        print(f"│  1  │   {calc.get_one_point_goals()} │   {calc.get_one_point_goals()} │")
        print(f"│  2  │   {calc.get_two_point_goals()} │   {calc.get_two_point_goals() * 2} │")
        print(f"│  3  │   {calc.get_three_point_goals()} │   {calc.get_three_point_goals() * 3} │")
        print("┌─────┐─────┐─────┐")
        print(f"│total│   {calc.get_total_score()} │   {calc.get_total_goals()} │")
        print("└─────┘─────┘─────┘")

        goal = int(input("1~3중 골 입력(0: 종료): "))
        if goal == 0:
            break
        
        points = int(input("골 입력: "))
        calc.add_goal(int(goal), points)
        
print("Game over!")
print("총 골수: {}".format(calc.get_total_score()))
print("총 점수: {}".format(calc.get_total_goals()))