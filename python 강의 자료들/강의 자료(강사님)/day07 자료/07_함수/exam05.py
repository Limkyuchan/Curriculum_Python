
def func(*args):
    size = args.__len__() #내장 함수 사용 시 len(args)
    for i in range(size):
        print('{0}번째 인자: {1}'.format(i, args[i]))
    print()

func(1,2,3)
func('hello', 'hi')
a = ['a', 2, 'b', 3]
func(a)
func(a, 'A')


