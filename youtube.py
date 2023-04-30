from pytube import YouTube

print('####### audio/video downloader #######')

link = input('Cole o link aqui:')
print('''

Digite 1 para baixar apenas o áudio;
Digite 2 para baixar o vídeo;
''')

option = int(input('---> :'))

yt = YouTube(link)

if option == 1:
    print('Opção escolhida: áudio')
    ys = yt.streams.get_audio_only()
elif option == 2:
    print('Opção escolhida: vídeo')
    ys = yt.streams.get_highest_resolution()

print('Título: ', yt.title)
print('Duração do vídeo: {} segundos'.format(yt.length))

print('\nBaixando...')

#ys.download(output_path='')
ys.download()

print('Download completo!')
