pesado = 0
leve = 0
q = int(input('Precisa registrar o peso de quantos itens?\n--->'))
for p in range(1, q + 1):
      peso = float(input(f'Qual o peso do {p}º item? --> '))
      if p == 1:
            pesado = peso
            leve = peso
            print(f'Único peso registrado: {peso}kg.\n')
      else:
            if peso > pesado:
                  pesado = peso
                  print(f'Mais leve: {leve}kg - Mais pesado: {pesado}kg\n')
            if peso < leve:
                  leve = peso
                  print(f'Mais leve: {leve}kg - Mais pesado: {pesado}kg\n')
            if peso > leve and peso < pesado:
                  print(f'Mais leve: {leve}kg - Mais pesado: {pesado}kg\n')
print('''
Dos {} pesos informados, {}kg foi o mais leve e {}kg o mais pesado.
'''.format(p,leve, pesado)
)

