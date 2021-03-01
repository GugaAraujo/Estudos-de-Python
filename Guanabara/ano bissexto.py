ano = int(input('Digite o ano: '))

amarelo = '\033[4;1;33m'
fecha = '\033[m'

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('É um ano {}bissexto{}!'.format(amarelo, fecha))
else:
    print('Não é um ano bissexto')