bus_stop = int(input('정거장 수 입력:'))
std_time = bus_stop < 10 and 2 or 4
total_time = bus_stop * std_time 

h = total_time//60
m = total_time%60

print_string = h and '총 소요시간은 {0}시간 {1}분 입니다.'.format(h, m) \
                    or '총 소요시간은 {0}분 입니다.'.format(m)
print(print_string)


