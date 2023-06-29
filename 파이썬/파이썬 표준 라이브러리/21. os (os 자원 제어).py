
# < os >
# 환경 변수나 디렉터리, 파일 등의 os 자원을 제어할 수 있게 해주는 모듈
# environ - 환경변수를 딕셔너리로 반환
# chdir() - 디렉터리 변경
# getcwd() - 현재 디렉터리 위치
# listdir() - 디렉터리 목록
# system() - os의 시스템 명령어 실행
# popen() - 명령의 실행결과를 읽기모드의 파일객체로 반환

import os

print(os.environ)
print(os.environ['PATH'])
print()

os.chdir('C:\\Windows')
print(os.getcwd())
os.chdir('System32')
print(os.getcwd())
print(os.listdir(os.getcwd()))
print()

os.chdir('C:\\')
os.system('dir')        #시스템(콘솔) 명령어 실행
f = os.popen('dir')     #실행 결과를 읽기모드의 파일형태로
print(f.read())