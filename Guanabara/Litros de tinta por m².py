print('\n#### Litros de tinta por M² ####\n')
alt = float(input('Qual a altura da parede a ser pintada? '))
larg = float(input('E a largura? '))

m2 = alt * larg
tinta = 2
rend = m2 / tinta
print('\nSua parede tem {}m². Se cada litro de tinta \npinta 2m², serão necessários {} litros de tinta'.format(m2, rend))


