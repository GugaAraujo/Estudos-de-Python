import datetime, time

print('\n=-=-= \033[1;0;33mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m =-=-=\n\n')

nom = input('Insira o nome do atleta: ')
nome = nom.title()
dia = datetime.date.today().day
meS = str(datetime.date.today().month)

if meS == '1':
    mes = meS.replace(meS,'Janeiro')
elif meS == '2':
    mes = meS.replace(meS,'Fevereiro')
elif meS == '3':
    mes = meS.replace(meS,'Março')
elif meS == '4':
    mes = meS.replace(meS,'Abril')
elif meS == '5':
    mes = meS.replace(meS,'Maio')
elif meS == '6':
    mes = meS.replace(meS,'Junho')
elif meS == '7':
    mes = meS.replace(meS,'Julho')
elif meS == '8':
    mes = meS.replace(meS,'Agosto')
elif meS == '9':
    mes = meS.replace(meS,'Setembro')
elif meS == '10':
    mes = meS.replace(meS,'Outubro')
elif meS == '11':
    mes = meS.replace(meS,'Novembro')
elif meS == '12':
    mes = meS.replace(meS,'Dezembro')

ano = datetime.date.today().year
nasc = int(input('Insira o ano de nascimento do atleta: '))
idade = ano - nasc


if idade < 9:
    res = 'Mirim'
elif idade < 14:
    res = 'Infantil'
elif idade < 19:
    res = 'Júnior'
elif idade < 20:
    res = 'Sênior'
elif idade < 100:
    res = 'Master'
elif idade >= 100:
    res = 'Matusalém'

time.sleep(2)

print(
'''

{} de {} de {}:

O atleta {} está com {} anos de idade e se enquadra na categoria {}.





'''.format(dia, mes, ano, nome, idade, res)
)
