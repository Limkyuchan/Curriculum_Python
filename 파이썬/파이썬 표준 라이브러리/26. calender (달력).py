
# < calender > 
# 파이썬에서 달력을 볼 수 있게 하는 도구
# calender.weekday
# - 연도, 월, 일을 받아 해당 날짜가 어떤 요일인지를 반환
# - 0(월요일) ~ 6(일요일)
#
# calender.monthrange
# - 연도, 월을 받아 해당 달의 1일이 무슨 요일인지와 며칠까지 인지를 반환(튜플) 

import calendar

print(calendar.calendar(2017))

print(calendar.prcal(2017))

print(calendar.prmonth(2017, 12))

print(calendar.weekday(2015, 1, 1))

print(calendar.monthrange(2016, 7))
print(calendar.monthrange(2017, 10))
print(calendar.monthrange(2023, 5))