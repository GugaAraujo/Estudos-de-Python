pri_term = int(input('Primeiro termo: '))
rz = int(input('Razão: '))

for c in range (pri_term, pri_term + (10 * rz), rz):
      print(c, end= ' - ')