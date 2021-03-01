nome = input('Qual seu nome?')
print('Bem vindo(a), {}!'.format(nome))
num = int(input('{}, digite um número:'.format(nome)))
print('O antecessor deste número é {}, e o sucessor {}.'.format(num - 1 , num + 1))
