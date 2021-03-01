print('\n#### Calcular 5% de desconto ####\n')
prod = (input('Qual o nome do produto? '))
val = float(input('Qual o preço do produto? '))
desc = val * 0.95


print('\nO produto {} estava com o preço em R${:.2f}. \nAplicado os 5% de desconto, passa a valer R${:.2f}'.format(prod, val, desc))


