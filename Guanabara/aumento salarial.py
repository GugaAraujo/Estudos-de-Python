print('\n#### Calcular 15% de aumento ####\n')
func = (input('Digite o nome do funcionário: '))
sal = float(input('Qual o salário atual de {}? '.format(func)))
dif = sal * 0.15
aum = sal + dif

print('\nO funcionário {} recebia R${:.2f}. Com o aumento \nde 15%, seu novo salário passa a ser {:.2f}.'.format(func, sal, aum))


