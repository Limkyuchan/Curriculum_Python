def func(n, s, **kargs):
    print(f'n:{n}')
    print(f's:{s}')
    keys = kargs.keys()
    i = 0
    for key in keys:
        print(f'{i}번째 인자{key}: {kargs[key]}')
        i += 1
    print()

func(n=123, s='test', a=10)

def func(**kargs):
    keys = kargs.keys()
    i = 0
    for key in keys:
        print(f'{i}번째 인자{key}: {kargs[key]}')
        i += 1
    print()

func(a=10)
func(a=1, b=2, c=3)
func(a='hello', b='hi')
func(a=['1', '2', 3], b=(1, 2, 3))


