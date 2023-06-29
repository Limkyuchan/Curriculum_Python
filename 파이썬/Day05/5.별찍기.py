
# 별 찍기

# Q1.
for i in range(5):
    print("*", end = "")
print()
print()

# Q2.
for i in range(5):
    print("*")
print()

# Q3.
for i in range(5):
    for j in range(5):
        print("*", end = "")
    print()
print()

# Q4.
for i in range(1,6):
    for j in range(5):
        print(i, end = "")
    print()
print()

# Q5.
for i in range(5):
    for j in range(1,6):
        print(j, end = "")
    print()
print()

# Q6.
for i in range(1,6):
    for j in range(5):
        print(i, end = "")
        i += 1
    print()
print()

# Q7.
for i in range(5, 0 ,-1):
    for j in range(5):
        print(i, end = "")
        i += 1
    print()
print()

# Q8.
# for i in range(1,6):
#     for j in range(i):
#         print("*", end = "")
#     print()
# print()

for i in range(1,6):
    print("*"*i)
print()

# Q9.
# for i in range(5, -1, -1):
#     for j in range(i):
#         print("*", end = "")
#     print()
# print()

for i in range(5):
    print("*"*(5-i))
print()

# Q10.
# for i in range(5, 0, -1):
#     print(" "*(5-i), end = "")
#     for j in range(i):
#         print("*", end = "")
#     print()
# print()

for i in range(5):
    print(" "*i + "*"*(5-i))
print()

# Q11.
# for i in range(4, -1, -1):
#     print(" "*i, end = "")
#     for j in range(5-i):
#         print("*", end = "")
#     print()
# print()

for i in range(1,6):
    print(" "*(5-i) + "*"*i)
print()

# Q12.
for i in range(1,6):
    print("*"*i)
for i in range(4,0,-1):
    print("*"*i)
print()

# Q13.
for i in range(5,0,-1):
    print("*"*i)
for i in range(2,6):
    print("*"*i)
print()

# Q14.
for i in range(5):
    print(" "* i + "*"* (5-i))
for i in range(2,6):
    print(" "*(5-i) + "*"*i)
print()

# Q15.
for i in range(1,6):
    print(" "* (5-i) + "*"*i)
for i in range(1,5):
    print(" "*i + "*"*(5-i))
print()

# Q16.
for i in range(1,6):
    print(" "*(5-i) + "*"*((i*2)-1))
print()

# Q17.
for i in range(5, 0, -1):
    print(" "*(5-i) + "*"*((i*2)-1) )
print()

# Q18.
for i in range(1,6):
    print(" "*(5-i) + "*"*((i*2)-1))
for i in range(4, 0, -1):
    print(" "*(5-i) + "*"*((i*2)-1))
print()

# Q19.
for i in range(5):
    print("*"*(5-i), end = "")
    print(" "*(2*(i+1)-1) + "*"*(5-i))
for i in range(2,6):
    print("*"*i, end = "")
    print(" "*(11-(i*2)) + "*"*i )
print()

# Q20.
for i in range(1,6):
    print("*"*i, end = "")
    print(" "*(11-(i*2)) + "*"*i)
for i in range(2,6):
    print("*"*(6-i), end = "")
    print(" "*((i*2)-1) + "*"*(6-i))
print()

# Q21.
for i in range(5, 0, -1):
    print(" "*(5-i) + "*"*((i*2)-1))
for i in range(2,6):
    print(" "*(5-i) + "*"*((i*2)-1))
print()