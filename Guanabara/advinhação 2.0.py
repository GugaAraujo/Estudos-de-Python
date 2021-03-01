import random, time
again = ''
listaalto = ['Chutou alto...: ', 'Passou um pouco...: ','Abaixa um pouco mais...: ']
listabaixo = ['Chutou baixo...: ', 'Faltou um pouco mais...: ', 'Levanta um pouco mais...: ']

while again != 'N':
    pc= random.randint(1, 10)
    print('\nPensei em um numero de 1 a 10. Tenta advinhar!')
    chute = int(input('\nPalpite: '))
    tentativa = 0
    while chute != pc:
        tentativa += 1
        if chute > pc:
            chute = int(input(random.choice(listaalto)))
        if chute < pc:
            chute = int(input(random.choice(listabaixo)))
    if chute == pc:
        #print('\nAcertou!\n')
        if tentativa > 0:
            print(f'\nVocê acertou com {tentativa+1} tentativas!\n')
        else:
            print('\nVocê acertou de primeira!\n')
    again = input('Quer Jogar de novo? [S/N]\n--->:').upper()[0]
if again == 'N':
    print('\nAté mais\n')
    time.sleep(1)
    for bye in range(1,5):
        print('.')
        time.sleep(0.3)
    print('''
        
        
        
        
        
        
''')
    exit()