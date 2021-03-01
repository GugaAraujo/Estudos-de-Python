import math
print('''
=================
 P O B R E S C O
=================''')

cinq = vin = dez = cinco = dois = um = 0
divcinq = divvin = divdez = divcinco = divdois = divum = 0

valor = int(input('Quer sacar quanto? R$ '))
while True:
    if valor % 50 == 0:
        divcinq = valor / 50
        cinq += divcinq
        break
    else:
        divcinq = valor / 50
        cinq += divcinq
        rcinq = valor - 50
        if rcinq % 20 == 0:
            divvin = rcinq / 20
            vin += divvin
            break
        else:
            divcinq = valor / 50
            cinq += divcinq
            rcinq = valor - 50
            divvin = rcinq / 20
            vin += divvin
            rvin = 20 - 10
            if rvin % 10 == 0:
                divdez = rvin / 10
                dez += divdez
                break
    print('Ainda to preso')
print(f'''
{cinq:.0f} de 50
{vin:.0f} de 20
{dez:.0f} de 10
{cinco} de 5
{dois} de 2
{um} de 1
''')

divcinq = valor / 50
cinq += divvin
divvin = valor / 20
vin += divvin
