import time
from pygame import mixer

print('\n\n##### Dragon Ball MP3 #####\n')

time.sleep(1.2)
print('Para ouvir o tema de Dragon Ball Z, digite 1.')
time.sleep(1.4)
print('Para ouvir o tema de Dragon Ball GT, digite 2:\n')
time.sleep(1.6)

m = int(input('Quero ouvir a número: '))

if m == 1:
    print('\nOuvindo Dragon Ball Z')
    mixer.init()
    mixer.music.load('z.mp3')
    mixer.music.play()
    input()
elif m == 2 :
    print('\nOuvindo Dragon Ball GT')
    mixer.init()
    mixer.music.load('gt.mp3')
    mixer.music.play()
    input()
else:
    print('\nOuvindo Dragon Ball GT')
    mixer.init()
    mixer.music.load('gt.mp3')
    mixer.music.play()
    input()

#não funciona
fim = input('teoricamente esse linha deve aparecer independete de sua escolha')