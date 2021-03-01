print('''Digite um número para calcularmos seu fatorial''')

n = 0
c = 0
while c != 1:
    n = int(input('---> '))
    print(f'Calculando {n}! = {n} x ', end='')
    for c in range(n - 1, 0, -1):
        if c == 1:
            print('{} = '. format(c), end='')
        else:
            print('{} x '.format(c), end='')
        n *=c
        c = -1
    print(f'{n}\n')






'''n = int(input('---> '))
    for c in range(n, 0, -1):
        resultado = n * (n-1)
        n += -1
        print(resultado,n)'''