n = int(input('\nDigite um número para obtermos sua tabuada: '))

print('\nTabuado do {}\n'.format(n))

for c in range (11):
    #print(c, f'x {n} = ',(c * n))
    print('{} x {:2} = {:2}'.format(n, c, (n * c)))


