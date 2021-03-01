from pytube import YouTube
import time

print(''' 
####### PegaTube #######
Baixador de áudio/video
''')

link = input('Cole o link aqui:')
print('''

Digite 1 para baixar apenas o áudio;
Digite 2 para baixar o vídeo;
''')
funcao = int(input('---> :'))
yt = YouTube(link)

if funcao == 1:
    print('Opção escolhida: áudio')
    yt = yt.extension('mp3')
    ys = yt.streams.get_audio_only()
elif funcao == 2:
    print('Opção escolhida: vídeo')
    ys = yt.streams.get_highest_resolution()


print('Título: ', yt.title)
print('ID do vídeo: {}'.format(yt.video_id))
print('Views: ', yt.views)
print('Duração do vídeo: {} segundos'.format(yt.length))
print('Avaliação do vídeo: {}'.format(yt.rating))

time.sleep(1.2)
print('\nBaixando...')

#definindo pastas: Importante por / antes do diretorio
ys.download(output_path='/Users\Gustavo\Desktop\youtube')

print('Download completo!')