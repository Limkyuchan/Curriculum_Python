import game.sound.echo
from game.graphic.render import render_test

game.sound.echo.echo_test()
render_test()

print()
###############################################
# import시 별칭 지정 가능 (as 별칭)
import game.sound.echo as gset
from game.graphic.render import render_test as ggrt

gset.echo_test()
ggrt()

###############################################
from game.sound import *
echo.echo_test()