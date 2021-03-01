import time
print('\n')
salario = int(input('Qual o seu salário? '))
limite = salario * 30 / 100
casa = int(input('Qual o valor do imóvel? '))
ano = int(input('Em quantos anos pretende financiar? '))
meses = (ano * 12)
parcela = casa / meses

time.sleep(0.8)
print('\ncalculando')
time.sleep(0.8)

print('''
Valor do imóvel: R${:.2f}.
Financiado em {} meses, em parcelas de R${:.2f}.
Salário atual: R${:.2f}
'''.format(casa, meses, parcela, salario))

time.sleep(2)
print('\ncalculando')
time.sleep(2)

aprovado = (
'''

A parcela não compromete mais do que 30% do seu salário,
por este motivo, seu financiamento está APROVADO!
Parabéns!
''')

reprovado = (
'''

Nestas condilções, o financiamento seria maior do que
30% de seu salário. Sugerimos escolher um imóvel de menor valor
ou período maior de financiamento para uma nova análise.
Com seu salário atual, procure parcelas menores do R${:.2f}
'''.format(limite)
)

if parcela < limite: print(aprovado)

else: print(reprovado)

