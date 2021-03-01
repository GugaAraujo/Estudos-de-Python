import random, time
print('\nBora jogar Par ou Impar!')
time.sleep(1)
poss = [0, 1]
pontuacao = 0
again = 'S'
recorde = 0
while again == 'S' or again == 'Q':
    while True:
        sorteio = random.randint(1, 100)
        n = int(input('\nDiz aí seu número: '))
        ip = (input('Par ou Impar [P/I]: ')).upper()
        if ip == 'P':
            jogador = 0
        elif ip == 'I':
            jogador = 1
        else:
            while True:
                ip = input('''Desculpe... Não entendi sua escolha.
    
Par ou Impar [P/I]: ''').upper()[0]
                if ip == 'P' or ip == 'I':
                    break
        print(f'\nEscolhi {sorteio}')
        print(f'\n{n} + {sorteio} = {n + sorteio}.')
        time.sleep(1)

        if (n + sorteio) % 2 != jogador:
            break

        print('Ou seja, você ganhou! Bora mais uma...')
        pontuacao += 1

    if pontuacao > recorde:
        recorde = pontuacao

    print(f'''Você perdeu.
    
Pontuação: {pontuacao}
Recorde: {recorde}
    ''')
    pontuacao = 0
    again = input('Quer tentar de novo?').upper()[0]
    if again == 'N':
        print('\nAté mais')
        exit()
    elif again == 'S' or again == 'Q':
        print('\nOk!', end='')
    elif again != 'Q' or again != 'S' or again != 'N':
        while True:
            again = input('''Desculpe... Não entendi sua escolha.
Deseja continuar?''').upper()[0]
            if again == 'Q' or again == 'S' or again == 'N':
                break
print('\n\nAté mais')
exit()