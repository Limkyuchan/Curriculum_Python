station_count = int(input('지하철역 수:'))
station_per_minute = 3
total_time = station_count * station_per_minute
total_hour = total_time // 60
total_minute = total_time % 60
print(f'{station_count}역 이동 총 소요시간:{total_hour}시간 {total_minute}분')

