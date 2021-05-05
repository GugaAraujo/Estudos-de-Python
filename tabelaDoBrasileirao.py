import time
times = ['Flamengo', 'Internacional', 'Atlético Mineiro', 'São Paulo', 'Fluminense', 'Grêmio',
          'Palmeiras', 'Santos', 'Athletico Paranaense', 'Bragantino', 'Ceará', 'Corinthians',
          'Atlético Goianense', 'Bahia', 'Sport', 'Fortaleza','Vasco', 'Goiás', 'Coritiba','Botafogo']
ultimos = times[-4::]

print(f'''
=-=-=-=-=-=-=-=-= Brasileirão =-=-=-=-=-=-=-=-=''')


menu = int(input('''
[1] - Pesquisar time na tabela
[2] - Mostrar os 5 melhores
[3] - Mostrar os 4 últimos classificados
[4] - Lista dos 20 classificados
[5] - Classificados por ordem alfabética
[0] - Sair

Digite sua opção ---> '''))

while True:
      if menu < 0 or menu > 5:
            print('Não entendi. Vamos tentar novamente.')
            time.sleep(1.5)
            menu = int(input('''
[1] - Pesquisar time na tabela
[2] - Mostrar os 5 melhores
[3] - Mostrar os 4 últimos classificados
[4] - Lista dos 20 classificados
[5] - Classificados por ordem alfabética
[0] - Sair

Digite sua opção ---> '''))
      if menu == 1:
            busca = input('\nDigite o time: ').strip().title()
            if busca not in times:
                  print(f'O time {busca} não está na lista deste ano.')
            else:
                  print(f'O {busca} ficou em {times.index(busca) + 1}º neste ano.')
            time.sleep(2)
            menu = int(input('''
[1] - Pesquisar time na tabela
[2] - Mostrar os 5 melhores
[3] - Mostrar os 4 últimos classificados
[4] - Lista dos 20 classificados
[5] - Classificados por ordem alfabética
[0] - Sair

Digite sua opção ---> '''))

      if menu == 2:
            print(f'''
5 primeiros colocados: {times[0:5]}
''')
            time.sleep(2)
            menu = int(input('''
[1] - Pesquisar time na tabela
[2] - Mostrar os 5 melhores
[3] - Mostrar os 4 últimos classificados
[4] - Lista dos 20 classificados
[5] - Classificados por ordem alfabética
[0] - Sair

Digite sua opção ---> '''))
      if menu == 3:
            print(f'''
4 últimos colocados: {ultimos[::-1]}
            ''')
            time.sleep(2)
            menu = int(input('''
[1] - Pesquisar time na tabela
[2] - Mostrar os 5 melhores
[3] - Mostrar os 4 últimos classificados
[4] - Lista dos 20 classificados
[5] - Classificados por ordem alfabética
[0] - Sair

Digite sua opção ---> '''))
      if menu == 4:
            print('\n')
            for c in range(len(times)):
                  print(f'{c + 1}º - {times[c]}')
            time.sleep(2)
            menu = int(input('''
[1] - Pesquisar time na tabela
[2] - Mostrar os 5 melhores
[3] - Mostrar os 4 últimos classificados
[4] - Lista dos 20 classificados
[5] - Classificados por ordem alfabética
[0] - Sair

Digite sua opção ---> '''))
      if menu == 5:
            print('\n')
            ordemalf = sorted(times)
            for alf in range(len(times)):
                  print(f'{ordemalf[alf]}: {times.index(ordemalf[alf])}º lugar')
            time.sleep(2)
            menu = int(input('''
[1] - Pesquisar time na tabela
[2] - Mostrar os 5 melhores
[3] - Mostrar os 4 últimos classificados
[4] - Lista dos 20 classificados
[5] - Classificados por ordem alfabética
[0] - Sair

Digite sua opção ---> '''))
      if menu == 0:
            break

time.sleep(.5)
print('\n...')
time.sleep(.5)
print('..')
time.sleep(.5)
print('.')
time.sleep(.5)
print('\nAté a próxima!\n\n')