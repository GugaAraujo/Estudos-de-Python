import random , time
time.sleep(.5)

n1 = random.randint (1 , 60)
n2 = random.randint (1 , 60)
while n2 == n1:
      n2 = random.randint(1, 60)
n3 = random.randint (1 , 60)
while n3 == n2 or n3 == n1:
      n3 = random.randint(1, 60)
n4 = random.randint (1 , 60)
while n4 == n3 or n4 == n2 or n4 == n1:
      n4 = random.randint(1, 60)
n5 = random.randint (1 , 60)
while n5 == n4 or n5 == n3 or n5 == n2 or n5 == n1:
      n5 = random.randint(1, 60)
n6 = random.randint (1 , 60)
while n6 == n5 or n6 == n4 or n6 == n3 or n6 == n2 or n6 == n1:
      n6 = random.randint(1, 60)

escolhidos = n1, n2, n3 , n4, n5 , n6
ordem = str(sorted(escolhidos))

print('''

### Mega Chute - Megasena ###''')

time.sleep(1)

print('''
--- \033[33mSua sorte de hoje é:\033[m ---''')

time.sleep(1)

print('''
=============================
\033[33m{}\033[m
=============================


-------- \033[33mBoa sorte!!\033[m --------






'''.format(ordem.replace(', ',' - ')))
