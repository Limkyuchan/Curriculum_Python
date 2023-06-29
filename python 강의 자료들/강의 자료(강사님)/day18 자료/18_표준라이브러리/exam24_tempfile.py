import tempfile

filename = tempfile.mkstemp('.temp', 'tmp_')
print(filename)

print('임시파일 생성 예제')
tmpfile = tempfile.TemporaryFile(prefix='tmp_', suffix='.temp', dir='C://pywork')
print(tmpfile.name)
print('파일생성 확인 후 엔터:')
input()
tmpfile.close()