def variableArgument_tupp(*args):
    print(args)
    print(type(args))

variableArgument_tupp('hello', 'hi')
variableArgument_tupp(1, 2, 3, 4, 5)
variableArgument_tupp(9, 8, 7)
ls = [9, 8, 7]
variableArgument_tupp(ls)
variableArgument_tupp(ls[0], ls[1], ls[2])
variableArgument_tupp(*ls)


def variableArgument_dict(**kargs):
    print(kargs)

variableArgument_dict(a=1, b=2, c=3)
variableArgument_dict(a={1:1}, b={2:2})
a={'1':10, '2':30, '3':20}
variableArgument_dict(**a)





