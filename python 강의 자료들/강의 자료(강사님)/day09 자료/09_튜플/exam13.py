# 튜플을 사용하여 도시의 이름과 위도, 경도를 저장하고, 
# 주어진 위치와 가장 가까운 도시를 찾는 프로그램

import math

# 도시들의 이름, 위도, 경도
cities = [
    ("New York", 40.7128, -74.0060),
    ("Los Angeles", 34.0522, -118.2437),
    ("Chicago", 41.8781, -87.6298),
    ("Houston", 29.7604, -95.3698),
    ("Miami", 25.7617, -80.1918)
]

# 대상 위치 (위도, 경도)
target_latitude = 39.7392
target_longitude = -104.9903

# 거리 계산 함수
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # 지구의 반지름 (km)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance

# 가장 가까운 도시 찾기
min_distance = float("inf")
closest_city = None
for city in cities:
    city_name, city_latitude, city_longitude = city
    distance = haversine(target_latitude, target_longitude, city_latitude, city_longitude)
    if distance < min_distance:
        min_distance = distance
        closest_city = city_name

# 결과 출력
print(f"The closest city to the target location is {closest_city}.")
