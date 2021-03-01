par = 0
impar = 0
print('\n\n')
for c in range(0, 6):
    n = int(input('Digite um número qualquer :'))
    if n % 2 == 0:
        par += n
    else:
        impar += n
print(f'\n\nA soma de número pares deu {par} e a dos ímpares foi de {impar}.''\n\n')