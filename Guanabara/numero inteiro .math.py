import random, math , time

time.sleep(0.5)

n = random.randint(1 , 100)
print('\nO computador escolherá um número aleatório de 1 a 100: ')

time.sleep(2.5)

print('\nNúmero escolhido: {}'.format(n), '\n')

raiz = math.sqrt(n)
trunc = math.trunc(raiz)

time.sleep(3)

print('A raiz quadrada do número sorteado é: {:.2f}'.format(raiz))
print('Este valor arredondado para cima é {} e para baixo {}.\n'.format(math.ceil(raiz) , math.floor(raiz)))

time.sleep(5)

print('Mas o que interessa é valor truncado: {}'.format(trunc))

time.sleep(4)

if trunc == 2:
      print('\nO número truncado, por acaso, é par.')
elif trunc == 4:
            print('\nO número truncado, por acaso, é par.')
elif trunc == 6:
      print('\nO número truncado, por acaso, é par.')
elif trunc == 8:
            print('\nO número truncado, por acaso, é par.')
elif trunc == 10:
            print('\nO número truncado, por acaso, é par.')
else:
      print('\nO número truncado, por acaso, é ímpar');

print('\n\n\n\n')

