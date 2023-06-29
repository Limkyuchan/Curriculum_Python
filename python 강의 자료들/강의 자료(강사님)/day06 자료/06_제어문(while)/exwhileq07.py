money = int(input("화폐 금액을 입력하세요: "))

# 각 화폐 종류별 변수
m50000 = money // 50000; money %= 50000
m10000 = money // 10000; money %= 10000
m5000 = money // 5000; money %= 5000
m1000 = money // 1000; money %= 1000
m500 = money // 500; money %= 500
m100 = money // 100; money %= 100
m50 = money // 50; money %= 50
m10 = money // 10

# 결과 출력
print(f"50000원 * {m50000}")
print(f"10000원 * {m10000}")
print(f"5000원 * {m5000}")
print(f"1000원 * {m1000}")
print(f"500원 * {m500}")
print(f"100원 * {m100}")
print(f"50원 * {m50}")
print(f"10원 * {m10}")
