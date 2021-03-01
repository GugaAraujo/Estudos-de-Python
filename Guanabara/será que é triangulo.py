import math

a = int(input('Digite a primeira reta: '))
b = int(input('Digite a segunda reta: '))
c = int(input('Digite a terceira reta: '))
print('\n'
      '')
if (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) or (c ** 2 == b ** 2 + a ** 2) == True:
    print('Deu triangulo retângulo!')
elif (a == b == c) == True:
    print('Temos um triangulo equilátero')
elif (a == b) or (b == c) or (c == a) == True:
    print('Com certeza se trata de um triângulo isósceles!')
elif (a != b !=c) and (b != a !=c) and (c != b != a) and (a < b +c) and (b < a + c) and (c < b + a) == True:
    print('Famoso Triângulo escaleno')
elif (a != b !=c) and (b != a !=c) and (c != b != a):
    print('Não formou triangulo')



'''if (a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2) == (a < b +c and b < a + c and c < b + a) == True:
    print('bateu')
else:
    print(('nops'))'''