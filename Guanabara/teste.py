nome = input('qual seu primeiro nome?')
sobrenome = input('Qual seu sobrenome?')


dia = (input('Qual seu dia de nascimento?'))
mes = int(input('Em qual mês você nasceu?'))

print('Olá {} {}, seu próximo aniversário será no dia {}/{} de 2021 \n\n'.format(nome,sobrenome,dia,mes))


print('Tá minusculo?', nome.islower())
print('Tá capitalizada?', sobrenome.istitle())
print('É un numero?', dia.isnumeric())
print('A classe primitiva de Mês É: {} '.format(type(mes)))