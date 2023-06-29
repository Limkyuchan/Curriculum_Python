def positive1(lst):
    result = []
    for i in lst:
        if i > 0:
            result.append(i)
    
    return result

print(positive1([1,-3,2,0,-5,6]))
print()

def positive2(lst):
    return lst > 0

d = [1,-3,2,0,-5,6]
n = list(filter(positive2, d))
print(n)
print()

positive3 = lambda x: x > 0
n = list(filter(positive3, [1,-3,2,0,-5,6]))
print(n)
print()

n = list(filter(lambda x: x > 0, [1,-3,2,0,-5,6]))
print(n)