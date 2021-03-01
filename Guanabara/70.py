qntd = soma = caro = 0
barato = 999999
nomecaro = nomebarato = ''

print('''
================
Vendinha Maneira
================
''')
while True:
    produto = input('Nome do produto: ').title()
    qntd += 1
    preço = float(input('Preço: R$ '))
    soma += preço
    if preço > caro:
        caro = preço
        nomecaro = produto
    if preço < barato:
        barato = preço
        nomebarato = produto
    again = input('Adicionar mais item a lista? [S/N] : ').upper()[0]
    while again not in 'SN':
        again = input('Adicionar mais item a lista? [S/N] :').upper()[0]
    if again == 'N':
        break

print(f'''
{qntd} itens cadastrados

Soma dos produtos: R$ {soma:.2f};
{nomebarato} é o item mais barato, custando R$ {barato:.2f};
{nomecaro} é o item mais caro, custando R$ {caro:.2f}''')
if caro >= (barato * 30 / 100):
    print(f'{nomecaro} tem um valor 30% maior do que {nomebarato}. ')