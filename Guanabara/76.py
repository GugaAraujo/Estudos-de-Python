list = ('detergente', 1.2, 'pasta de dente', 1.98, 'sabonete', 2.0, 'desodorante', 7.11)
print(f'{"LISTA DE PREÇOS"::^37}')
for c in range(len(list)):
      if c % 2 == 0:
            print(f'{list[c]:.<30}', end='')
      if c % 2 == 1:
            print(f'R${list[c]:>5.2f}')