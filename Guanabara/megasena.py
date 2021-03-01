import random , time
loop = 0
time.sleep(1.2)

n1 = random.randint (1 , 60)
n2 = random.randint (1 , 60)
n3 = random.randint (1 , 60)
n4 = random.randint (1 , 60)
n5 = random.randint (1 , 60)
n6 = random.randint (1 , 60)

print('\n\n#### Mega Chute - Megasena ####\n')

print('---- Sua sorte de hoje é: -----\n')

loop = 0
time.sleep(2)

print('===============================\n'
      '- {:2} - {:2} - {:2} - {:2} - {:2} - {:2} -\n'
      '===============================\n\n'
      '--------- Boa sorte!! ---------\n\n\n\n'.format(n1 , n2 , n3 , n4 , n5, n6))
