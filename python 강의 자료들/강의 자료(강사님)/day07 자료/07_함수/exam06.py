def func(n, s, *args):
    print(f'n:{n}')
    print(f's:{s}')
    for ar in args:
        print(ar)
    print()

func(1,2,3)
func('hello', 'hi')
a = ['a', 2, 'b', 3]
func(a, 'A')
#func(a) # s에 들어갈 인자가 없음 func() missing 1 required positional argument: 's'

def func(*args, n, s):
    print(f'n:{n}')
    print(f's:{s}')
    for ar in args:
        print(ar)
    print()

func(1,2,3, n=10, s=20)
func('hello', s='hi', n=123)
a = ['a', 2, 'b', 3]
func(a, s='A', n=10)
#func(a) # s에 들어갈 인자가 없음 func() missing 1 required positional argument: 's'

