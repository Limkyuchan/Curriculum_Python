#태어난 년도를 2자리로 또는 4자리로 입력하여 나이를 구하는 함수 정의

import datetime

def yearToAge(year):
    if not year.isdigit():      return -1
    else:                       year = int(year)

    fy = datetime.datetime.now().year
    sy = fy % 100
    if year >= 0 and year < 100:
        if year < sy:
            age = sy - year
        else:
            age = (100+sy) - year
    elif year >= 1900 and year < 3000:
        age = fy - year
    return age
    
print(yearToAge('1999'))
print(yearToAge('89'))
print(yearToAge('1976'))
print(yearToAge('2002'))
print(yearToAge('aa'))
