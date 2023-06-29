value = 0
def recu():
    global value
    print('\t'*value, end="")
    print(f'[value:{value}] 재귀!')
    if value == 3:
        print('\t'*value, value, 'Function End!')
        return
    value += 1
    recu()
    value -= 1
    print('\t'*value, value, 'Functionimage.png End!')

recu()

