pri_term = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
cnt = 1
menu = 10
while menu != 0:
      if menu > 0:
            cnt = 1
            while cnt <= menu:
                  pri_term += rz
                  cnt += 1
                  print(f'{pri_term} -> ', end='')
            print('pausa\n')
      menu = int(input('Quantos termos gostaria de ver agora? '))
print('\nBye!\n\n')