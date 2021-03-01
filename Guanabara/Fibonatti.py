t1 = 0
t2 = 1
cont = 3
n = int(input('''
--- Sequência de Fibonacci ---

Quantos termos gostaria de ver?
---> '''))
print(f'{t1} -> {t2} -> ', end='')
while cont <= (n - 1):
      cont += 1
      t3 = t1 + t2
      t1 = t2
      t2 = t3
      print(f'{t3} -> ', end='')
while cont <= n:
      cont += 1
      t3 = t1 + t2
      t1 = t2
      t2 = t3
      print(f'{t3}')
print('\nFim')


