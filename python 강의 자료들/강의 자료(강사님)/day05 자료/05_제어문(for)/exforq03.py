musicTime = 230

playTime = int(input('재생시간 : '))

playingTime = playTime*100/musicTime
progress = '';
print('┌', end="")
print('─'*10,end="")
print('┐')
progressBar = '│'
# progressBar = ''
for i in range(0, int(playingTime/10)):
    progressBar += '■'
progressBar += '{0:02d}%'.format(int(playingTime))
for i in range(int(playingTime/10)+3, 10):
    progressBar +=' '
if int(playingTime/10)<8:
    progressBar +='│'
print(progressBar)
print('└'+('─'*10)+'┘')

 