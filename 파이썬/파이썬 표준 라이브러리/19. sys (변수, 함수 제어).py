
# < sys >
# 파이썬 인터프리터가 제공하는 변수와 함수를 제어하는 기능을 가진 모듈
# 주요 기능
# - sys.argv - 프로그램 실행 시 전달받은 인자에 접근
# - sys.exit - ctrl + c, ctrl + z 등과 같은 기능
# - sys.path - 파이썬 모듈이 저장되어 있는 위치 정보 (append 하여 추가 가능)

import sys

print(sys.argv)
print(sys.path)
sys.exit()
print('종료됨') # 죽은 코드