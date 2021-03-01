qntd = homem = mulher = acima = macima = 0
resposta = ''
while True:
    resposta = input('\nGostaria de cadastrar uma pessoa [S/N]: ').upper()[0]
    while resposta not in 'SN':
        resposta = input('\nGostaria de cadastrar uma pessoa [S/N]: ').upper()[0]
    if resposta == 'N':
        break
    print(f'''
{'=' * (len('CADASTRE UMA PESSOA'))}
CADASTRE UMA PESSOA
{'=' * (len('CADASTRE UMA PESSOA'))}
    ''')
    idade = int(input('Idade: '))
    sexo = input('Qual o sexo [M/F]:').upper()[0]
    qntd += 1
    while sexo not in 'MF':
        sexo = input('Qual o sexo [M/F]:').upper()[0]
    if sexo == 'F' and idade >= 20:
        mulher += 1
        macima += 1
    elif sexo == 'F' and idade < 20:
        mulher +=1
    elif idade >= 18:
        acima += 1

    if resposta == 'N':
        break
print(f'''
    Quantidade:             {qntd};
    Homens:                 {qntd - mulher}
    Mulheres:               {mulher}
    Mulheres acima de 20:   {macima}
    Pessoas acima de 18:    {acima}
    ''')