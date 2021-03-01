import time
from pygame import mixer

print('\n\n##### Dragon Ball MP3 #####\n')

time.sleep(1.2)

print('Ouvindo Dragon Ball Z')
mixer.init()
mixer.music.load('z.mp3')
mixer.music.play()
input()

print('xiu')


