from game.sound import *
#game.sound의 __init__.py파일에 외부에서 import 할 수 있는 이름을 등록해야 함

echo.echo_test() 

wav.wav_test() # __init__.py파일에 등록되지 않은 모듈은 포함되지 않음