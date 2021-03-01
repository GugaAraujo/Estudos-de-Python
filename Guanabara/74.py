
tupla = (int(input('Digita aí um número:')),
int(input('Digita aí um número:')),
int(input('Digita aí um número:')),
int(input('Digita aí um número:')))

print(tupla)
print(f'O maior valor é {max(tupla)}')
print(f'O menor valor é {min(tupla)}')
print('O número 9 apareceu {} vezes.'.format(tupla.count(9)))
if 3 in tupla:
    print('O número 3 está na {}º posição'.format(tupla.index(3) + 1))
else:
    print('Não há número 3 na tupla')
print('Os números pares: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')