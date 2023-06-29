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
os.system('dir') #시스템(콘솔) 명령어 실행
f = os.popen('dir') #실행 결과를 읽기모드의 파일형태로
print(f.read())