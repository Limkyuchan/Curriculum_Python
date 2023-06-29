n = chr(97)
print(n)

n = chr(68)
print(n)

n = ord('A')
print(n)

n = ord('d')
print(n)

alpha_u = [chr(ch) for ch in range(ord('A'), ord('Z')+1)]
alpha_l = [chr(ch) for ch in range(ord('a'), ord('z')+1)]
alpha = alpha_u + alpha_l
print()

print('아스키 코드와 문자')
for ascii in range(0, 128):
    print(f'[{ascii:3}] : [{chr(ascii):3}]')