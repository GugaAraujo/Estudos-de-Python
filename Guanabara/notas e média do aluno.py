print('\n###### lançamento de notas ######')
print('Média mínima para aprovação: 6.0\n')
#corte = float(input('Qual a média mínimma para aprovação?'))

nome = input('Digite o nome do aluno:')
p1 = float(input('Digite a nota do primeiro bimestre:'))
p2 = float(input('Digite a nota do segundo bimestre:'))
p3 = float(input('Digite a nota do terceiro bimestre:'))
p4 = float(input('Digite a nota do quarto bimestre:'))
media = float((p1 + p2 + p3 + p4) / 4)
print('\nNome: {};\n 1º Bi: {};\n 2º Bi: {};\n 3º Bi: {};\n 4º Bi: {};\n'.format(nome , p1 , p2 , p3 , p4))
print('A média de {} foi de {}.\n'.format(nome , media))

if media >= 6:
    print('Situação: Aprovado.')
else:
    print('Situação: Reprovado.')
