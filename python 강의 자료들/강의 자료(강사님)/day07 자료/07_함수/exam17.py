calc_final_price = lambda price, discount: round(price * (1 - discount), 2)

print(calc_final_price(10000, 0.1))
print(calc_final_price(10000, 0.2))
print(calc_final_price(10000, 0.25))
