import random , time

a1 = input('Insira o nome do aluno 1:')
a2 = input('Insira o nome do aluno 2:')
a3 = input('Insira o nome do aluno 3:')
a4 = input('Insira o nome do aluno 4:')

escolha = random.randint(1, 4)
time.sleep(0)
print('\nO aluno sorteado pelo IF foi:\n')
time.sleep(0)

if escolha == 1: print(a1)
elif escolha == 2: print(a2)
elif escolha == 3: print(a3)
elif escolha == 4: print(a4)

#Refiz com metodo choise
alunos = [a1, a2, a3, a4]
choise = random.choice(alunos)
print('Escolhido pelo método Choise é : {}'.format(choise))

random.shuffle(alunos)
print('A sequencia é: {}'.format(random.shuffle(alunos)))