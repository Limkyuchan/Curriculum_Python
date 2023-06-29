
# OOP & Class

# Q1. 농구 점수 계산기 만들기 (클래스 이용)
# 생성자를 이용해서 count 값 초기화하기 (0 또는 임의의 값으로 초기화)
# getter, setter 사용하여 사용자 임의로 초기화가 가능하도록 작성
# 기능)
# 1,2,3점 메뉴 입력 시 해당 골과 득점 입력
# 각각 골의 수와 총 골의 수 개별 누적
# 프로그램 종료 시(경기 종료) 총점과 총 골 수 출력


class Basketball:

    def __init__(self, point1 = 0, point2 = 0, point3 = 0):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3

    def basketballGame(self):

        while True:
            goal = int(input("골 입력(종료시 0): "))
            self.goalCount(goal)

            if goal == 0:
                break
            
    def goalCount(self, goal):
        
        if goal == 0:
            self.resultGame()

        elif goal == 1:
            self.__point1 += 1

        elif goal == 2:
            self.__point2 += 1

        elif goal == 3:
            self.__point3 += 1

        else:
            print("점수 입력 오류!")

    def resultGame(self):
        self.totalScore = (self.__point1 * 1) + (self.__point2 * 2) + (self.__point3 * 3)
        self.totalCount = self.__point1 + self.__point2 + self.__point3

        print()
        print("="*23)
        print("      │ 골 │  점수")
        print("─"*23)
        print(f" 1점  │\t{self.__point1}  │\t{self.__point1 * 1}")
        print(f" 2점  │\t{self.__point2}  │\t{self.__point2 * 2}")
        print(f" 3점  │\t{self.__point3}  │\t{self.__point3 * 3}")
        print("─"*23)
        print(f"total │\t{self.totalCount}  │\t{self.totalScore}")
        print("="*23)
        print()

    @property
    def point1(self):
        return self.__point1

    @property
    def point2(self):
        return self.__point2
    
    @property
    def point3(self):
        return self.__point3
    
    @point1.setter
    def point1(self, point1):
        self.__point1 = point1

    @point2.setter
    def point2(self, point2):
        self.__point2 = point2

    @point3.setter
    def point3(self, point3):
        self.__point3 = point3 

record = Basketball()

record.point1 = 100
record.basketballGame()