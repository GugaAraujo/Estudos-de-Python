import datetime
print(f'''\033[33m
{'='* len('C o n t r o l e   d e   g l i c e m i a')}\033[m
C o n t r o l e   d e   g l i c e m i a
\033[33m{'='* len('C o n t r o l e   d e   g l i c e m i a')}\033[m
''')

lmedia = 120
ljejum = 95
lrefei = 140

jejum = int(input('Indice em jejum: '))
if jejum >= ljejum:
    print(f'\033[33m**\033[mValor em jejum acima do limite de {ljejum} mg/dl\n')
cafe = int(input('Indice após o café da manhã: '))
if cafe >= lrefei:
    print(f'\033[33m**\033[mValor pós prandial acima do limite de {lrefei} mg/dl\n')

almoço = int(input('Indice após o almoço: '))
if almoço >= lrefei:
    print(f'\033[33m**\033[mValor pós prandial acima do limite de {lrefei} mg/dl\n')

janta = int(input('Indice após a janta: '))
if janta >= lrefei:
    print(f'\033[33m**\033[mValor pós prandial acima do limite de {lrefei} mg/dl\n')

mediadia = (jejum + cafe + almoço + janta) / 4

print(f'''
================
 {datetime.datetime.today().day} do {datetime.date.today().month} de {datetime.date.today().year}
================''')
print(
f'''
A média dos índices do dia ficou em {mediadia} mg/dL''')
if mediadia > lmedia:
    print(f'Sua média diária está acima do limete. Excedido em {mediadia - lmedia} mg/dL.')
if mediadia < lmedia:
    print(f'Sua média diária ficou {lmedia - mediadia} mg/dL abaixo do limite.')
if mediadia == lmedia:
    print('Sua média diária está no limite.')