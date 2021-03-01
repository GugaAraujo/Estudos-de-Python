extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinto'

numero = int(input('Digite um número de 0 a 5: '))
while True:
      if numero < 0 or numero > 5:
            numero = int(input('Digite um número de 0 a 5: '))
      else:
            break
print(f'Você digitou {extenso[numero]}')