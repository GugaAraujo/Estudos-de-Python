import time
time.sleep(1)
print('\n=-=-=-= Calculadora de IMC =-=-=-=')
time.sleep(1)
alt = float(input('\nQual sua altura? '))
peso = float(input('Qual seu peso? '))

imc = peso / (alt * alt)

if imc < 18.5:
    res = 'Abaixo do peso'
elif imc < 24.9:
    res = ('Peso normal')
elif imc < 29.9:
    res = ('Sobrepeso')
elif imc < 34.9:
    res = ('Obesidade Grau I')
elif imc < 39.9:
    res = ('Obesidade Grau II')
elif imc >= 39.9:
    res = ('Obesidade Grau III')

print(
'''
Seu IMC é: {:.1f} e está classificado como {}.
'''.format(imc, res))

time.sleep(2)
if imc >= 25: print('O ideal no seu caso era crescer uns 3 metros. xD')
time.sleep(2)

