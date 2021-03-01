
qntd = 0
soma = 0
digitado = 0
print('\nPara sair, digite 999\n')
while digitado != 999:
      if digitado < 999:
            digitado = int(input('Digite um número: '))
            qntd += 1
            soma += digitado
      if digitado == 999:
            soma -= 999
            qntd -= 1
print(f'{qntd} Nºs digitados. Soma dos Nºs: {soma}')