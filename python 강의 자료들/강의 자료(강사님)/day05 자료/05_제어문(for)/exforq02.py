inputCm = int(input('길이 입력(cm) : '))

rulerCm = 30

print('┌', end="")
print('─'*29,end="")
print('┐')

print('│'*31, end="")
print()
for i in range(0, 31):
    if i == inputCm:
        print('↑', end="")
    else:
        print(' ', end="")