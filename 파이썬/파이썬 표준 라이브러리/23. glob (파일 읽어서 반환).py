
# < glob > 
# 디렉터리 내의 파일들을 읽어서 반환하는 기능의 모듈
# *, ? 등의 메타 문자를 써서 원하는 파일만 읽어 들일 수도 있다.

import glob

print(glob.glob('C:\\Windows\System*'))

# C:\\windows\ 폴더에서 system으로 시작되는 파일만
["C:\\windows\\system", "C:\\windows\\system.ini", "C:\\windows\\System32"]