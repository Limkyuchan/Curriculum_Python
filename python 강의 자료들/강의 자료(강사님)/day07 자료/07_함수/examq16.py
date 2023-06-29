# 실습1 (등속운동 계산)
calculate_velocity = lambda distance, time: distance / time

print(calculate_velocity(100, 1), 'm/s') # 100m를 1초에 갔다면
print(calculate_velocity(100, 10), 'km/m') # 100km를 10분에 갔다면
print(calculate_velocity(100, 5), 'km/h') # 100km를 5시간에 갔다면

# 실습2 (짝수 판별)
is_even = lambda number: number % 2 == 0

print(is_even(123))
print(is_even(124))

# 실습3 (큰 수)
find_max = lambda num1, num2: max(num1, num2)

print(find_max(1, 2))
print(find_max(2, 1))
print(find_max(2, 2))

# 실습4 (문자열 비교)
compare_strings = lambda str1, str2: str1 == str2

print(compare_strings('hello', 'hi'))
print(compare_strings('hello', 'hello'))


# 실습5 (리스트 요소의 합)
calculate_sum = lambda numbers: sum(numbers)

print(calculate_sum([1,2,3,4,5]))
print(calculate_sum([1,2,3]))
