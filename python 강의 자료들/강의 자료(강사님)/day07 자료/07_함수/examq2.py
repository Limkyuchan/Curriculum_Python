#태어난 년도를 2자리로 입력하여 나이를 구하는 함수 정의

import datetime

def yearToAge(year):
    if not year.isdigit():      return -1
    else:                       year = int(year)

    y = datetime.datetime.now().year % 100

    if year > 100 or year < 0:  return -1
    else:
        if year < y:       age = y - year
        else:               age = (100+y) - year
        return age

print(yearToAge('99'))
print(yearToAge('89'))
print(yearToAge('02'))
print(yearToAge('aa'))
