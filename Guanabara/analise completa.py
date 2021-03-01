import datetime, time
ano = datetime.date.today().year
somaidade = 0
novo = 0
velho = 0
homem = 0
menino = 0
mulher = 0
menina = 0
adulto = 0
for q in range(1, 6):
    print(f'\n=-=-=-=-=-= {q}ª Pessoa =-=-=-=-=-=')
    nome = input('Nome: ').title()
    nasc = int(input('Ano de nascimento:'))
    idade = ano - nasc
    if q == 1:
        novo = idade
        anciao = nome
        baby = nome
        velho = idade

    else:
        if idade < novo:
            novo = idade
            baby = nome
        if idade > velho:
            velho = idade
            anciao = nome
    somaidade += idade
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Escolha entre Masculino ou Feminino: ').strip().upper()[0]
        if sexo == 'F':
                mulher += 1
                if idade < 18:
                    menina += 1
                if idade > 18:
                    adulto += 1
        if sexo == 'M':
                homem += 1
                if idade < 18:
                    menino += 1
                if idade > 18:
                    adulto += 1
    print(f'Idade: {idade}, Sexo: {sexo}')

criança = (menina + menino)
idademedia = somaidade / q

print('\n')
for sleep in range(3):
    time.sleep(1)
    print('.')

print(f'''
Dados das {q} pessoas cadastradas:

Mulheres: {mulher}; Homens: {homem}; Adultos: {adulto};
Crianças: {criança}, sendo {menina} meninas e {menino} meninos;

A média de idade é de {idademedia:.0f};
A pessoa mais nova tem {novo} anos e chama-se {baby};
A pessoa mais velha tem {velho} anos e chama-se {anciao}



''')