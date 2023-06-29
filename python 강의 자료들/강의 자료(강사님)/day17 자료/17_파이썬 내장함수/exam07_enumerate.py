lst = ['body', 'foo', 'bar']

for i, name in enumerate(lst):
    print(i, name)
print()

dt = {'body':'A', 'B':'foo', 'bar':'C'}
for i, e in enumerate(dt):
    print(i, e, dt[e])