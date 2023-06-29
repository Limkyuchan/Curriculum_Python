from random import randrange

def lotto_generator():
    numset = set()
    while len(numset) < 7:
        numset.add(randrange(1, 46))
    return sorted(list(numset))

def lotto_dict_generator(n):
    lotto_dict = {}
    for i in range(1, n+1):
        nums = lotto_generator()
        bonus = nums.pop(randrange(0, 7))
        lotto_dict[i] = (nums, bonus)
    return lotto_dict

def lotto_output(filename, lotto_dict):
    with open(filename, 'w', newline='') as f:
        for k, nums in lotto_dict.items():
            tmp = list(nums[0])
            tmp.insert(0, k)
            tmp.append(nums[1])
            tmp = str(tmp).replace('[', '').replace(' ', '').replace(']', '|')
            f.write(tmp)


lotto_dict = lotto_dict_generator(100)
lotto_output('로또.txt', lotto_dict)

"""
로또.txt
1,20,27,36,37,41,43,42|2,20,28,29,30,34,36,38|3,3 ...
"""