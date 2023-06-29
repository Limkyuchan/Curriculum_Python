
# < threading >
# threading.Thread 클래스 상속 및 구현 예제
# - threading.Thread.__init__ 메서드 호출 필수
# - 새로운 스래드에서 동작할 run 메서드 정의

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data

    def run(self): # start()호출 시 새로운 thread로 동작할 메서드
        for i in self.data:
            print(i)
            time.sleep(0.1)

upper = [chr(ch) for ch in range(ord('A'), ord('Z')+1)]
lower = [chr(ch) for ch in range(ord('a'), ord('z')+1)]

th1 = MyThread(upper)
th2 = MyThread(lower)

th1.start()
th2.start()