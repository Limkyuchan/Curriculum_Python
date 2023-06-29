
def lotto_input(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return data

def freq_counter(num_list):
    freq = {k:0 for k in range(1, 46)}

    for num in num_list:
        num = num.split(',')
        for idx in num[1:7]:
            freq[int(idx)] += 1
    return freq

def freq_output(filename, freq):
    with open(filename, 'w') as f:
        for k, v in freq.items():
            f.write(f'{k}:{v},')


data = lotto_input('로또.txt')
num_list = data.split('|')
freq = freq_counter(num_list)
freq_output('빈도.txt', freq)

"""
빈도.txt
1:18,2:13,3:7,4:17,5:10,6:10,7:21,8:11,9:19, ...
"""