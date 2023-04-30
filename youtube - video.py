from pytube import YouTube

print('####### Youtube Downloader #######')

link = input('Cole o link aqui:')
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()

print('Título: ', yt.title)
print('Duração do vídeo: {} segundos'.format(yt.length))

print('\nBaixando...')

#definindo pastas: Importante por / antes do diretorio
#ys.download(output_path='')
ys.download()

print('Download completo!')
