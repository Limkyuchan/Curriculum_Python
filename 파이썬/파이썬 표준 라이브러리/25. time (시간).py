
# < time >
# 시간과 관련된 모듈
# - sleep() - 일정 시간 동안 멈추는 기능
#           - 주로 반복 루프에서 사용


import time

t = time.time()
print('현재시간(1970.01.01.00.00기준):', t)

lt = time.localtime(t)
print(lt)

at = time.asctime(lt)
print(at)

ct = time.ctime() #위 작업을 한 번에
print(ct)

print()
print('%a:', time.strftime('%a',  lt), "-요일 이름 줄임말")
print('%A:', time.strftime('%A',  lt), "-요일 이름")
print('%b:', time.strftime('%b',  lt), "-달 이름 줄임말")
print('%B:', time.strftime('%B',  lt), "-달 이름")
print('%c:', time.strftime('%c',  lt), "-날짜와 시간")
print('%d:', time.strftime('%d',  lt), "-날(day)")
print('%H:', time.strftime('%H',  lt), "-시간(24시간)")
print('%I:', time.strftime('%I',  lt), "-시간(12시간)")
print('%j:', time.strftime('%j',  lt), "-1년 중 누적날짜")
print('%m:', time.strftime('%m',  lt), "-달")
print('%M:', time.strftime('%M',  lt), "-분")
print('%p:', time.strftime('%p',  lt), "-AM/PM")
print('%S:', time.strftime('%S',  lt), "-초")
print('%U:', time.strftime('%U',  lt), "-1년 중 누적 주(일요일 시작기준)")
print('%w:', time.strftime('%w',  lt), "-숫자 요일(0:일요일)")
print('%W:', time.strftime('%W',  lt), "-1년 중 누적 주(월요일 시작기준)")
print('%x:', time.strftime('%x',  lt), "-현재 설정된 로케일 기반 날짜")
print('%X:', time.strftime('%X',  lt), "-현재 설정된 로케일 기반 시간")
print('%Y:', time.strftime('%Y',  lt), "-년도")
print('%Z:', time.strftime('%Z',  lt), "-시간대(대한민국 표준시)")
print('%y:', time.strftime('%y',  lt), "-세기 제외한 년도")

for i in range(10):
    print(i)
    time.sleep(1)
