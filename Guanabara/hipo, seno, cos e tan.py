import math , time
#print('Calculadora de Hipotenusa')
#ca = float(input('Insira o cateto adjacente: '))
#co = float(input('Insira o cateto oposto: '))
#hip = math.hypot(ca, co)

#print(hip)
print('\n\nPara calcular:\n\n'
      'Hipotenusa - Digite 1:\n'
      'Seno - Digite 2\n\n'
      )
eita = int(input('Digite:'))

if eita == 1:
    print('\nCalculadora de Hipotenusa\n')
    ca = float(input('Insira o cateto adjacente: '))
    co = float(input('Insira o cateto oposto: '))
    hip = math.hypot(ca, co)
    print('hipotenusa: {:.2f}'.format(hip))

elif eita == 2:
        angulo = float(input('Digite o angulo: '))
        seno = math.sin(math.radians(angulo))
        cosseno = math.cos(math.radians(angulo))
        tangente = math.tan(angulo)
        print('O seno do angulo {:.0f}ºé {:.2f} .'.format(angulo, seno))
        print('O cosseno é {:.3f} e a tangente é {:.3f}.'.format(cosseno, tangente))

else : print('\n\nÑ NTNDR')
