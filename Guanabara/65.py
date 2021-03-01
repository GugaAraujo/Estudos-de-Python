import time
perg = ''
qntd = soma = 0
entrada = int(input('Digite um número: '))
maior = entrada
menor = entrada
qntd += 1
soma += entrada
while perg != 'N':
    perg = input('Quer digitar mais um? ').upper()[0]
    if perg == 'S':
        entrada = int(input('Digite um número: '))
        qntd += 1
        soma += entrada
        if entrada > maior:
            maior = entrada
        if entrada < menor:
            menor = entrada
    if perg == 'N':
        print('\nCalculando...\n')
        time.sleep(2)
print(f'''
Quantidade de números lidos: {qntd};
Soma dos números lidos:      {soma};
Média dos números lidos:     {soma / qntd};
O menor número lido foi:     {menor};
O maior número lido foi:     {maior};

''')