import random, time

print('Jóóóóó')
time.sleep(1)
print('Keeeeen')
time.sleep(1)
print('Pô!\n')

opcoes = ['pedra', 'papel', 'tesoura']
pc = random.choice(opcoes)

user = input('Faça sua escolha: ')
useR = user.lower()
ganhei = ['Chupa que é de uva!', 'Senta que é de menta!', 'Ganhei! Má Oiii! Haha hihi']
perdi = ['Perdi... :(', 'Deixei você ganhar!', 'Deu sorte hoje. Parabéns!']
emp = ['Empatamos.', 'Deu na mesma.', 'Nem pra mim, nem pra você.']


int = '\nEu havia escolhido {}. Então...'.format(pc)

if pc == 'pedra' and useR == 'tesoura' or pc == 'tesoura' and useR == 'papel' or pc == 'papel' and useR == 'pedra':
    print(int, random.choice(ganhei))
elif pc == 'pedra' and useR == 'papel' or pc == 'tesoura' and  useR == 'pedra' or pc == 'papel' and useR == 'tesoura':
    print(int, random.choice(perdi))
elif pc == useR:
    print(int, random.choice(emp))
elif useR != 'pedra' or 'papel' or 'tesoura':
    print('\nEscreve direito, poxa...')
    exit()
else: print('Situação não prevista. Avise o Gustavo!  ===> ALERTA GERAL <=== CHAMANDO TODAS AS UNIDADES!')

print('\n')