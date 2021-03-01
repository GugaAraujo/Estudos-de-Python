import time
n1 = 0
n2 = 0
menu = ''

for c in range(1, 3):
    n = int(input(f'Digite o {c}º número: '))
    if c == 1:
        n1 += n
    else:
        n2 += n
print(f'\nNº digitados: {n1} e {n2}\n')
while menu != 6:
    menu = int(input(
'''=-=-=-= Menu =-=-=-=
[1] Somar
[2] Multiplicar
[3] Média
[4] Maior e menor
[5] Novos números
[6] Sair
=-==-=-=-=-=-=-=-=-=
    
---> '''))
    if menu == 1:
        print(f'\nA soma de {n1} e {n2} é {n1 + n2}\n')
    elif menu == 2:
        print(f'\nO produto de {n1} por {n2} é {n1 *n2}\n')
    elif menu == 3:
        print(f'\nA média de {n1} e {n2} é {(n1 + n2) / 2}\n')
    elif menu == 4:
        if n1 > n2:
            print(f'\nO menor número é {n2} e o maior é {n1}\n')
        if n2 > n1:
            print(f'\n O menor número é {n1} e o maior é {n2}\n')
    elif menu == 5:
        for c in range(1, 3):
            n = int(input(f'\nDigite o {c}º número: '))
            if c == 1:
                n1 = 0
                n1 += n
            else:
                n2 = 0
                n2 += n
        print(f'\nNº digitados: {n1} e {n2}\n')
    elif menu == 6:
        print('\n\nAté mais!\n\n')
        exit()
    else:
        print('\nOpçâo inválida\n')