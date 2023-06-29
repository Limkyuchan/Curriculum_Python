
# < threading >
# 두가지 이상의 작업을 동시에 수행할 수 있도록 해주는 기능의 모듈
# - target : 실행할 모듈
# - args : targe에 전달할 인자
# - daemon thread 여부
# - start() 새로운 스레드로 지정된 모듈 동작

import threading
import time

def say(msg):
    while True:
        time.sleep(1)
        print(msg)

for msg in ['you', 'need', 'python']:
    t = threading.Thread(target=say, args=(msg,))
    t.daemon = True
    t.start()

for i in range(100):
    time.sleep(0.1)
    print(i)