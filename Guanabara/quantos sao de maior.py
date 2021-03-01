import datetime
ano = datetime.datetime.today().year


maior = 0
menor = 0
for c in range(1, 8, 1):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = ano - nasc
    maioridade = 18
    if idade > maioridade:
        print(f'idade: {idade} anos;\nAtinguiu a maioridade.\n')
        maior += 1
    else:
        print(f'idade: {idade} anos;\nFaltam {maioridade - idade} anos para atingir a maioridade.\n')
        menor += 1
print('''Quantidade de maiores: {}
Quantidade de menores: {}'''.format(maior, menor))