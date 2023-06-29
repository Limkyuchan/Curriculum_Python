
# < tempfile >
# 임시파일을 만들 때 사용하는 모듈
# - tempfile.mktemp()는 중복되지 않는 임시 파일의 이름을 무작위로 생성
# - prefic, suffix 등을 설정하여 무작위 이름 앞 뒤에 붙을 문자지정 가능

import tempfile

filename = tempfile.mkstemp('.temp', 'tmp_')
print(filename)

print('임시파일 생성 예제')
tmpfile = tempfile.TemporaryFile(prefix='tmp_', suffix='.temp', dir='C://pywork')
print(tmpfile.name)
print('파일생성 확인 후 엔터:')
input()         # 파일 확인 후 콘솔에서 enter 입력하면 close()함수의 동작으로 생성된 임시파일 삭제됨
tmpfile.close() 

