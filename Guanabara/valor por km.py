import time


km = int(input('Informe a distância em Km/h: '))
print('\n')
time.sleep(0.8)
print('Calculando...\n')
time.sleep(1.2)

if km <= 200:
    taxa = 0.50
    print('O valor cobrado pela corrida será de R${:.2f}.'.format(km * taxa))
else :
    taxa = 0.45
    print('O valor cobrado pela corrida será de R${:.2f}.'.format(km * taxa))
time.sleep(1.2)
print('\nFim\n\n\n')