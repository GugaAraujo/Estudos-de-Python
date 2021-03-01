import datetime, time

print('\n=-=-= \033[1;0;32mA L I S T A M E N T O - M I L I T A R\033[m =-=-=')
print('=-=-=-=-= \033[1;0;33mRepública do Leite Condensado\033[m =-=-=-=-=\n\n')
nom = input('Insira seu nome: ')
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
nasc = int(input('Insira seu ano de nascimento: '))
idade = ano - nasc
limite = 18
multa = 38.40

if idade < limite:
    exc = limite - idade
    res = 'Ainda faltam {} anos para seu alistamento.'.format(exc)
elif idade == limite:
    res = 'Você completa {} anos em {}, momento de se alistar ao Exército.'.format(limite, ano)
elif idade >= limite:
    exc = idade - limite
    res = '''
Seu alistamento está atrasado em {} anos.
Multa por ano atrasado: R${:.2f};
Total a pagar: R${:.2f}'''.format(exc, multa, multa * exc)




time.sleep(2)

print(
'''

{} de {} de {}:

{}: {} anos;
{}







'''.format(dia, mes, ano, nome, idade, res)
)
