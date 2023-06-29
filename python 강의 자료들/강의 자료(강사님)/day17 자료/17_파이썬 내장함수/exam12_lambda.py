mysum = lambda a, b:a+b
print(mysum(1, 2))

mylist = [lambda a,b:a+b, lambda a,b:a*b]
print(mylist[0](3,4))
print(mylist[1](3,4))