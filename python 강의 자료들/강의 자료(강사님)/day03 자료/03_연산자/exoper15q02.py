CRI_STATION = 7
STD_TIME1 = 3
STD_TIME2 = 2
ZERO = 0

station_stop = int(input('정거장 수 입력:'))
over_station = station_stop > CRI_STATION and station_stop - CRI_STATION or ZERO
station_stop = over_station > ZERO and station_stop - over_station or station_stop

time1 = STD_TIME1 * station_stop
time2 = over_station > ZERO and STD_TIME2 * over_station or ZERO

total_time = time1 + time2

h = total_time//60
m = total_time%60

print_string = h and '총 소요시간은 {0}시간 {1}분 입니다.'.format(h, m) \
                    or '총 소요시간은 {0}분 입니다.'.format(m)
print(print_string)

