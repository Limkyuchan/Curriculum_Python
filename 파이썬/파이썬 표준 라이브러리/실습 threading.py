
import time
import threading

class Running(threading.Thread):

    def __init__ (self, name):
        threading.Thread.__init__(self)
        self.move = name + ":"

    def run(self):
        for i in range(7):
            self.move = self.move + "*"
            time.sleep(0.7)
            print(self.move)

a = Running("John")
b = Running("Jessi")

a.start()
b.start()