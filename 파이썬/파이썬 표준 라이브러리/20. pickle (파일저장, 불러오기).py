
# < pickle > 
# 객체의 형태를 그대로 파일에 저장하고 불러올 수 있게 하는 모듈
# dump - 저장하기
# load - 불러오기

import pickle

f = open('test.txt', 'wb')
data = {1:'python', 2:'you need'}
pickle.dump(data, f)
f.close()

f = open('test.txt', 'rb')
data = pickle.load(f)
print(data)