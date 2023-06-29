def two_times(x):
    return x*2

n = list(map(two_times, [1,2,3,4]))
print(n)

n = list(map(lambda a:a+1, n))
print(n)