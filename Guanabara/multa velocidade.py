import time


vel = int(input('Informe a velocidade do veículo em Km/h: '))
print('\n')

leve = 60
grave = 80
multa = 7

time.sleep(1.2)
print('Calculando...\n')
time.sleep(1.2)

if vel <= leve:
    print('Velocidade abaixo da média.')
    time.sleep(1.2)
    print('Boa viagem!')
elif vel <= grave:
    lim = grave
    exc = (vel - lim)
    print('Velocidade acima da média: Infração leve')
    time.sleep(1.2)
    print('Valor da Multa por cada Km excedido: R$ 7,00;')
    time.sleep(1.2)
    print('O motorista receberá multa no valor de R${:.2f}.'.format((vel - leve) * 7))
elif vel > grave:
    lim = grave
    exc = (vel - lim)
    print('Alta velocidade: Infração grave!')
    time.sleep(1.2)
    print('Valor da Multa por cada Km excedido: R$ 18,00;')
    time.sleep(1.2)
    print('O motorista receberá multa no valor de R${:.2f}.'.format((vel - grave) * 18))
    time.sleep(1.2)
    print('O motorista deve ser sua CNH cassada.')

time.sleep(1.2)
print('\nFim\n\n\n')