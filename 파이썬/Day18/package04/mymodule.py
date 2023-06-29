
"""
이것은 내가 만든 모듈

"""
# mymodule.py

def mysum(n1, n2):
    return n1 + n2

def mymin(n1, n2):
    return n1 - n2


print("mymodule.__name__ : ", __name__)

if __name__ == "__main__":
    print("mymodule에 작성된 내부 코드")

# mymodule 을 직접 실행할 때의 이름이 __main__ 이기 때문에
# mymodule 파일을 직접 실행할 때만 (작성된 내부 코드)가 출력되게 된다.