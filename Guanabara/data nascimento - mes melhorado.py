usuario =input('\n\nInfome seu nome: ')
nometitle = usuario.title()
dia = int(input('Em qual dia do mês foi sua última menstruação?'))
mes = str(input('Qual o mês da última menstruação?'))
mesM = mes.upper()
ano = int(input('Digite o ano:'))
erro = 'Data Incorreta'

#ano bissexto:
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    bissexto = True
else:
    bissexto = False


#Replace dos meses

#novembro corrigido
if mesM == 'NOVEMBRO' and dia <= 25:
    data = (dia) + 7
    trocames = mesM.replace(mesM, 'Agosto')
elif mesM == 'NOVEMBRO' and dia == 25:
    data = 1
    trocames = mesM.replace(mesM, 'Setembro')
elif mesM == 'NOVEMBRO' and dia == 26:
    data = 2
    trocames = mesM.replace(mesM,'Setembro')
elif mesM == 'NOVEMBRO' and dia == 27:
    data = 3
    trocames = mesM.replace(mesM,'Setembro')
elif mesM == 'NOVEMBRO' and dia == 28:
    data = 4
    trocames = mesM.replace(mesM,'Setembro')
elif mesM == 'NOVEMBRO' and dia == 29:
    data = 5
    trocames = mesM.replace(mesM,'Setembro')
elif mesM == 'NOVEMBRO' and dia == 30:
    data = 6
    trocames = mesM.replace(mesM,'Setembro')
elif mesM == 'NOVEMBRO' and dia > 30:
    data = erro
    trocames = mesM.replace(mesM,'Setembro')

#Dezembro Corrigido
elif mesM == 'DEZEMBRO' and dia <= 24:
    data = (dia) + 6
    trocames = mesM.replace(mesM,'Setembro')
elif mesM == 'DEZEMBRO' and dia == 25:
    data = 1
    trocames = mesM.replace(mesM,'Outubro')
elif mesM == 'DEZEMBRO' and dia == 26:
    data = 2
    trocames = mesM.replace(mesM,'Outubro')
elif mesM == 'DEZEMBRO' and dia == 27:
    data = 3
    trocames = mesM.replace(mesM,'Outubro')
elif mesM == 'DEZEMBRO' and dia == 28:
    data = 4
    trocames = mesM.replace(mesM,'Outubro')
elif mesM == 'DEZEMBRO' and dia == 29:
    data = 5
    trocames = mesM.replace(mesM,'Outubro')
elif mesM == 'DEZEMBRO' and dia == 30:
    data = 6
    trocames = mesM.replace(mesM,'Outubro')
elif mesM == 'DEZEMBRO' and dia == 31:
    data = 7
    trocames = mesM.replace(mesM,'Outubro')
elif mesM == 'DEZEMBRO' and dia >= 31:
    data = erro
    trocames = mesM.replace(mesM,'Outubro')

#Janeiro Corrigido
elif mesM == 'JANEIRO' and dia <= 6:
    data = (dia) + 6
    trocames = mesM.replace(mesM,'Outubro')
elif mesM == 'JANEIRO' and dia == 26:
    data = 1
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'JANEIRO' and dia == 27:
    data = 2
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'JANEIRO' and dia == 28:
    data = 3
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'JANEIRO' and dia == 29:
    data = 4
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'JANEIRO' and dia == 30:
    data = 5
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'JANEIRO' and dia == 31:
    data = 6
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'JANEIRO' and dia >= 31:
    data = erro
    trocames = mesM.replace(mesM,'Novembro')




elif mesM == 'FEVEREIRO' and bissexto == True and dia == 23:
    data = 1
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == True and dia == 24:
    data = 2
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == True and dia == 25:
    data = 3
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == True and dia == 26:
    data = 4
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == True and dia == 27:
    data = 5
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == True and dia == 28:
    data = 6
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == True and dia == 29:
    data = 7
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == True and dia > 29:
    data = erro
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == False and dia == 22:
    data = 1
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == False and dia == 23:
    data = 2
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == False and dia == 24:
    data = 3
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == False and dia == 25:
    data = 4
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == False and dia == 26:
    data = 5
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == False and dia == 27:
    data = 6
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == False and dia == 28:
    data = 7
    trocames = mesM.replace(mesM,'Novembro')
elif mesM == 'FEVEREIRO' and bissexto == False and dia > 28:
    data = erro
    trocames = mesM.replace(mesM,'Novembro')

elif mesM == 'MARÇO':
    trocames = mesM.replace(mesM,'Dezembro')
elif mesM == 'ABRIL':
    trocames = mesM.replace(mesM,'Janeiro')
elif mesM == 'MAIO':
    trocames = mesM.replace(mesM,'Fevereiro')
elif mesM == 'JUNHO':
    trocames = mesM.replace(mesM,'Março')
elif mesM == 'JULHO':
    trocames = mesM.replace(mesM,'Abril')
elif mesM == 'AGOSTO':
    trocames = mesM.replace(mesM,'Maio')
elif mesM == 'SETEMBRO':
    trocames = mesM.replace(mesM,'Junho')
elif mesM == 'OUTUBRO':
    trocames = mesM.replace(mesM,'Julho')





#somadia = (7)
#data = (dia) + somadia


print('\n{}, provavelmente seu bebê chegará no dia {} de {}!\nParabéns, Mamãe!!'.format(nometitle, data, trocames))
print(bissexto)


