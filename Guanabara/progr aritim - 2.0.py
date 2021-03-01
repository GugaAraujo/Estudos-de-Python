pri_term = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
cnt = 1

while cnt <= 10:
      pri_term += rz
      cnt += 1
      print(f'{pri_term} -> ', end='')