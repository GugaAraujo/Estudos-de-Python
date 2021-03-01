from pytube import YouTube
import time

print(''' 
####### PegaTube #######
Baixador de audio/video

Digite 1 para baixar apenas o audio;
Digite 2 para baixar o vídeo;
''')

funcao = input('---> :')

link = input('Cole o link aqui:')
yt = YouTube(link)
ys = yt.streams.get_audio_only()

print('Título: ', yt.title)
print('Views: ', yt.views)
print('Duração do vídeo: {} segundos'.format(yt.length))
print('Avaliação do vídeo: {}'.format(yt.rating))

time.sleep(1.2)
print('\nBaixando...')

#definindo pastas: Importante por / antes do diretorio
ys.download(output_path='/Users\Admin\Desktop\youtube')

print('Download completo!')