import random
min = int(input('Digite um número minimo:'))
max = int(input('Digite um número maximo:'))
num = random.randint(min,max)

chute = int(input('\nEu escolhi um número, de {} a {}.\nTente descobrir:'.format(min, max)))


if chute > num:
    print('Chutou alto...')
elif chute == num:
    print('Tu é bom nisso! Parabéns')
elif chute < num:
    print('Chutou baixo...')