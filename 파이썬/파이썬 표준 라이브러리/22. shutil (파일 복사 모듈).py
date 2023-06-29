
# < shutil >
# 파일 복사 모듈
# 복사 후 복사된 파일명 반환
# 동일한 파일명이 있다면 덮어쓴다.

import shutil

ret = shutil.copy('test.txt', 'dst.txt')
print(ret)
